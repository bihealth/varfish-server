/*
Build state machine for managing the background filtering job.
 */

// Define states
const STATE_INITIAL = 'initial';
const STATE_IDLE = 'idle';
const STATE_GET_JOB_ID = 'get-job-id';
const STATE_WAIT_JOB_RESULTS = 'wait-job-results';

// Define events
const EVENT_START = 'start';
const EVENT_GOT_JOB_ID = 'got-job-id';
const EVENT_STILL_WAITING = 'still-waiting';
const EVENT_GOT_RESULT = 'got-result';
const EVENT_CANCEL = 'cancel';
const EVENT_SUBMIT = 'submit';
const EVENT_NO_JOB_ID = 'no-job-id';
const EVENT_ERROR = 'error';

// Other global variables to manage the state machine.
let currentState = STATE_INITIAL;
let ajaxCall = null;
let filterButton = $("#submitFilter");
let resultsTable = $("#resultsTable");
let timer = null;


/*
Handle form error responses from Django AJAX JSON response.
*/

let INPUT_TAB_AFFILIATION = {
  'genotype-tab': [
    /_gt$/
  ],
  'frequency-tab': [
    /^thousand_genomes_/,
    /^exac_/,
    /^gnomad_genomes_/,
    /^gnomad_exomes_/,
  ],
  'effect-tab': [
  ],
  'quality-tab': [
    /_dp_het$/,
    /_dp_hom$/,
    /_ab$/,
    /_gq$/,
    /_ad$/,
    /_fail$/
  ],
  'blacklist-tab': [
    /^gene_blacklist$/,
    /^gene_whitelist$/,
    /^genomic_region$/
  ],
  'flags-tab': [
    /^flag_/
  ],
  'clinvar-tab': [
    /^require_in_/,
    /^clinvar_include_/
  ],
  'export-tab': [
    /export/,
    /^file_type$/
  ],
  'misc-tab': [
    /^result_rows_limit$/
  ],
  'settings-tab': [
    /^settingsDump$/
  ]
};
INPUT_TAB_AFFILIATION['more-tab'] = $.merge(
  $.merge(
    $.merge(
      $.merge(
        [],
        INPUT_TAB_AFFILIATION['clinvar-tab'],
      ),
      INPUT_TAB_AFFILIATION['export-tab']
    ),
    INPUT_TAB_AFFILIATION['misc-tab']
  ),
  INPUT_TAB_AFFILIATION['settings-tab']
);

function findTabToInput(input) {
  let result = [];
  $.each(INPUT_TAB_AFFILIATION, function(key, value) {
    $.each(value, function(index, pattern) {
      if (pattern.test(input)) {
        result.push(key);
      }
    });
  });
  return result;
}

function updateTableDisplay() {
  $("#table-config").attr("class",
    "display-" + $("#result-display-frequencies").val()
  );
  $('[data-toggle="tooltip"]').tooltip();
  $('[data-toggle="popover"]').popover();
}

function displayConnectionError() {
  currentState = STATE_IDLE;
  resultsTable.empty();
  resultsTable.html(
    '<div class="alert alert-danger sodar-alert-top">' +
    '<i class="fa fa-exclamation-triangle"></i> ' +
    'Error in request. Probably the server is not responding or offline.' +
    '</div>');
}

// Helper function to switch the state of the submit button (make it "Submit").
function animateFilterButtonSubmit() {
  let icon = $("i", filterButton).clone();
  filterButton.text(" Filter & Display");
  icon.prependTo(filterButton);
  filterButton.attr("data-event-type", EVENT_SUBMIT);
  icon.removeClass("fa-spin");
}

// Helper function to switch the state of the submit button (make it "Cancel").
function animateSubmitButtonCancel() {
  let icon = $("i", filterButton).clone();
  filterButton.text(" Cancel");
  icon.prependTo(filterButton);
  filterButton.attr("data-event-type", EVENT_CANCEL);
  resultsTable.empty();
  resultsTable.load(
    $(filterButton).data("url-wheel"),
    function(responseText, textStatus, request) {
      if (textStatus == "error") {
        // stop spinning action on error
        resultsTable.empty();
        animateFilterButtonSubmit();
        currentState = STATE_IDLE;
        switch (request.status) {
          case 0:
            displayConnectionError();
            break;
          default:
            console.log("Error during AJAX call: ", request, textStatus, responseText);
        }
      }
    }
  );
  icon.addClass("fa-spin");
}

function doVisualErrorResponseOnTabs(data) {
  $.each(data, function(element_name, error_texts) {
    let tabs = findTabToInput(element_name);
    $.each(tabs, function(index, tab) {
      $("#" + tab).addClass("border border-danger");
    });
  });
}

function doVisualErrorResponseOnForms(data) {
  $.each(data, function(element_id, error_texts) {
    let element = $("#id_" + element_id);
    let text = "";
    $.each(error_texts, function(index, error) {
      text += error + "<br />";
    });
    element.addClass("border border-danger");
    element.attr('data-toggle', 'tooltip');
    element.attr('title', "");
    element.attr('data-original-title', text);
    element.attr('data-html', 'true');
    element.tooltip({trigger : 'hover'});
  });
}

function removeVisualErrorResponse() {
  $(".border, .border-danger").each(function(index) {
    $(this).removeClass("border border-danger");
  });
}

// Handle state INITIAL
function handleEventStateInitial(eventType, event) {
  if (eventType == EVENT_START) {
    currentState = STATE_GET_JOB_ID;
    animateSubmitButtonCancel();
    ajaxCall = $.ajax({
      type: "GET",
      dataType: "json",
      url: filterButton.data('url-request-last-job'),
      success: function(result) {
        let filter_job_uuid = result['filter_job_uuid'];
        if (filter_job_uuid) {
          return handleEvent(EVENT_GOT_JOB_ID, {'filter_job_uuid': filter_job_uuid});
        }
        return handleEvent(EVENT_NO_JOB_ID, null);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        resultsTable.empty();
        animateFilterButtonSubmit();
        switch (jqXHR.status) {
          case 0:
            displayConnectionError();
            break;
          default:
            console.log("Error during AJAX call: ", jqXHR, textStatus, errorThrown);
            handleEvent(EVENT_ERROR, null);
        }
      }
    });
  } else {
    console.log("unexpected event", eventType, event, "in state", currentState);
  }
}

// Handle state IDLE
function handleEventStateIdle(eventType, event) {
  if (eventType == EVENT_SUBMIT) {
    currentState = STATE_GET_JOB_ID;
    animateSubmitButtonCancel();
    removeVisualErrorResponse();
    let data = $("#filterForm").serializeArray().reduce(
      (accumulator, current) => (accumulator[current.name] = current.value, accumulator), {}
    );
    data[filterButton.attr("name")] = filterButton.attr("value");
    ajaxCall = $.ajax({
      type: "POST",
      dataType: "json",
      url: filterButton.data("url"),
      data: data,
      success: function (result) {
        handleEvent(EVENT_GOT_JOB_ID, {'filter_job_uuid': result['filter_job_uuid']});
      },
      error: function(jqXHR, textStatus, errorThrown) {
        resultsTable.empty();
        animateFilterButtonSubmit();
        switch (jqXHR.status) {
          case 0:
            displayConnectionError();
            // aborted ajax call.
            break;
          case 400:
            removeVisualErrorResponse();
            doVisualErrorResponseOnForms(jqXHR.responseJSON);
            doVisualErrorResponseOnTabs(jqXHR.responseJSON);
            handleEvent(EVENT_ERROR, null);
            break;
          default:
            console.log("Error during AJAX call: ", jqXHR, textStatus, errorThrown);
            handleEvent(EVENT_ERROR, null);
        }
      }
    });
  } else {
    console.log("unexpected event", eventType, event, "in state", currentState);
  }
}

// Handle state GET_JOB_ID
function handleEventStateGetJobId(eventType, event) {
  if (eventType == EVENT_GOT_JOB_ID) {
    currentState = STATE_WAIT_JOB_RESULTS;
    ajaxCall = $.ajax({
      type: "POST",
      dataType: "json",
      url: filterButton.data("url-status"),
      data: event,
      success: function (data) {
        if (data['status'] == 'done') {
          return handleEvent(EVENT_GOT_RESULT, event);
        }
        return handleEvent(EVENT_STILL_WAITING, event);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        resultsTable.empty();
        animateFilterButtonSubmit();
        switch (jqXHR.status) {
          case 0:
            displayConnectionError();
            break;
          default:
            console.log("Error during AJAX call: ", jqXHR, textStatus, errorThrown);
            handleEvent(EVENT_ERROR, null);
        }
      }
    });
  } else if (eventType == EVENT_NO_JOB_ID) {
    currentState = STATE_IDLE;
    animateFilterButtonSubmit();
    clearTimeout();
    resultsTable.empty();
  } else if (eventType == EVENT_CANCEL) {
    currentState = STATE_IDLE;
    if (ajaxCall) {
      ajaxCall.abort("Aborting AJAX call ...");
      ajaxCall = null;
    }
    clearTimeout();
    resultsTable.empty();
    animateFilterButtonSubmit();
  } else if (eventType == EVENT_ERROR) {
    currentState = STATE_IDLE;
    animateFilterButtonSubmit();
    clearTimeout();
    resultsTable.empty();
  } else {
    console.log("unexpected event", eventType, event, "in state", currentState);
  }
}

// Handle state WAIT_JOB_RESULTS
function handleEventStateWaitJobResults(eventType, event) {
  if (eventType == EVENT_STILL_WAITING) {
    timer = setTimeout(
      function(event, eventData) {
        currentState = STATE_GET_JOB_ID;
        handleEvent(event, eventData);
      },
      5000,
      EVENT_GOT_JOB_ID, event
    );
  } else if (eventType == EVENT_CANCEL) {
    currentState = STATE_IDLE;
    if (timer) {
      clearTimeout(timer);
      timer = null;
    }
    if (ajaxCall) {
      ajaxCall.abort("Aborting AJAX call ...");
      ajaxCall = null;
    }
    resultsTable.empty();
    animateFilterButtonSubmit();
  } else if (eventType == EVENT_ERROR) {
    currentState = STATE_IDLE;
    clearTimeout();
    resultsTable.empty();
    animateFilterButtonSubmit();
  } else if (eventType == EVENT_GOT_RESULT) {
    let data = {
      "csrfmiddlewaretoken": csfr_token,
      "filter_job_uuid": event["filter_job_uuid"]
    };
    ajaxCall = $.ajax({
      url: filterButton.data("url-reload"),
      method: "POST",
      data: data,
      success: function(data) {
        currentState = STATE_IDLE;
        animateFilterButtonSubmit();
        resultsTable.html(data);
        updateTableDisplay();
      },
      error: function(jqXHR, textStatus, errorThrown) {
        resultsTable.empty();
        animateFilterButtonSubmit();
        switch (jqXHR.status) {
          case 0:
            displayConnectionError();
            break;
          default:
            console.log("Error during AJAX call: ", jqXHR, textStatus, errorThrown);
            handleEvent(EVENT_ERROR, null);
        }
      }
    });
  }
  else {
    console.log("unexpected event", eventType, event, "in state", currentState);
  }
}

// Event handler function
function handleEvent(eventType, event) {
  if (currentState == STATE_INITIAL) {
    return handleEventStateInitial(eventType, event);
  } else if (currentState == STATE_IDLE) {
    return handleEventStateIdle(eventType, event);
  } else if (currentState == STATE_GET_JOB_ID) {
    return handleEventStateGetJobId(eventType, event);
  } else if (currentState == STATE_WAIT_JOB_RESULTS) {
    return handleEventStateWaitJobResults(eventType, event);
  } else {
    console.log("unexpected state", currentState)
  }
}