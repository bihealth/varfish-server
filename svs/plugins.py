from projectroles.plugins import ProjectAppPluginPoint
from bgjobs.plugins import BackgroundJobsPluginPoint

from .models import Case, StructuralVariantComment, StructuralVariantFlags
from .urls import urlpatterns


class ProjectAppPlugin(ProjectAppPluginPoint):
    """Plugin for registering app with Projectroles"""

    name = "svs"
    title = "SVs"
    urls = urlpatterns
    # ...

    icon = "hospital-o"

    entry_point_url_id = "variants:case-list"

    description = "Structural Variants"

    #: Required permission for accessing the app
    app_permission = "variants.view_data"

    #: Enable or disable general search from project title bar
    search_enable = False

    #: List of search object types for the app
    search_types = []

    def get_object_link(self, model_str, uuid):
        """
        Return URL for referring to a object used by the app, along with a
        label to be shown to the user for linking.
        :param model_str: Object class (string)
        :param uuid: sodar_uuid of the referred object
        :return: Dict or None if not found
        """
        obj = self.get_object(eval(model_str), uuid)

        if isinstance(obj, StructuralVariantComment):
            return {"url": obj.get_absolute_url(), "label": obj.shortened_text()}
        elif isinstance(obj, StructuralVariantFlags):
            return {"url": obj.get_absolute_url(), "label": obj.human_readable()}
        elif isinstance(obj, Case):
            return {"url": obj.get_absolute_url(), "label": obj.name}

        return None
