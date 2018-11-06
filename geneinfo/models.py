from django.db import models
from postgres_copy import CopyManager


class Hgnc(models.Model):
    hgnc_id = models.CharField(max_length=16)
    symbol = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    locus_group = models.CharField(max_length=32, null=True)
    locus_type = models.CharField(max_length=32, null=True)
    status = models.CharField(max_length=32, null=True)
    location = models.CharField(max_length=64, null=True)
    location_sortable = models.CharField(max_length=64, null=True)
    alias_symbol = models.CharField(max_length=128, null=True)
    alias_name = models.CharField(max_length=512, null=True)
    prev_symbol = models.CharField(max_length=128, null=True)
    prev_name = models.CharField(max_length=1024, null=True)
    gene_family = models.CharField(max_length=256, null=True)
    gene_family_id = models.CharField(max_length=32, null=True)
    date_approved_reserved = models.CharField(max_length=32, null=True)
    date_symbol_changed = models.CharField(max_length=32, null=True)
    date_name_changed = models.CharField(max_length=32, null=True)
    date_modified = models.CharField(max_length=16, null=True)
    entrez_id = models.CharField(max_length=16, null=True)
    ensembl_gene_id = models.CharField(max_length=32, null=True)
    vega_id = models.CharField(max_length=32, null=True)
    ucsc_id = models.CharField(max_length=16, null=True)
    ena = models.CharField(max_length=64, null=True)
    refseq_accession = models.CharField(max_length=128, null=True)
    ccds_id = models.CharField(max_length=256, null=True)
    uniprot_ids = models.CharField(max_length=256, null=True)
    pubmed_id = models.CharField(max_length=64, null=True)
    mgd_id = models.CharField(max_length=256, null=True)
    rgd_id = models.CharField(max_length=32, null=True)
    lsdb = models.CharField(max_length=1024, null=True)
    cosmic = models.CharField(max_length=32, null=True)
    omim_id = models.CharField(max_length=32, null=True)
    mirbase = models.CharField(max_length=16, null=True)
    homeodb = models.CharField(max_length=16, null=True)
    snornabase = models.CharField(max_length=16, null=True)
    bioparadigms_slc = models.CharField(max_length=32, null=True)
    orphanet = models.CharField(max_length=16, null=True)
    pseudogene_org = models.CharField(max_length=32, null=True)
    horde_id = models.CharField(max_length=16, null=True)
    merops = models.CharField(max_length=16, null=True)
    imgt = models.CharField(max_length=32, null=True)
    iuphar = models.CharField(max_length=32, null=True)
    kznf_gene_catalog = models.CharField(max_length=32, null=True)
    namit_trnadb = models.CharField(max_length=16, null=True)
    cd = models.CharField(max_length=16, null=True)
    lncrnadb = models.CharField(max_length=32, null=True)
    enzyme_id = models.CharField(max_length=64, null=True)
    intermediate_filament_db = models.CharField(max_length=32, null=True)
    rna_central_ids = models.CharField(max_length=32, null=True)
    objects = CopyManager()

    class Meta:
        indexes = [
            models.Index(fields=["ensembl_gene_id"]),
            models.Index(fields=["entrez_id"]),
        ]


class Mim2geneMedgen(models.Model):
    omim_id = models.IntegerField()
    entrez_id = models.CharField(max_length=16, null=True)
    omim_type = models.CharField(max_length=32, null=True)
    source = models.CharField(max_length=32, null=True)
    medgen_cui = models.CharField(max_length=8, null=True)
    comment = models.CharField(max_length=64, null=True)
    objects = CopyManager()

    class Meta:
        indexes = [models.Index(fields=["entrez_id"])]


class Hpo(models.Model):
    database_id = models.CharField(max_length=16)
    name = models.CharField(max_length=1024, null=True)
    qualifier = models.CharField(max_length=4, null=True)
    hpo_id = models.CharField(max_length=16, null=True)
    reference = models.CharField(max_length=128, null=True)
    evidence = models.CharField(max_length=4, null=True)
    onset = models.CharField(max_length=16, null=True)
    frequency = models.CharField(max_length=16, null=True)
    sex = models.CharField(max_length=8, null=True)
    modifier = models.CharField(max_length=16, null=True)
    aspect = models.CharField(max_length=1, null=True)
    biocuration = models.CharField(max_length=32, null=True)
    objects = CopyManager()

    class Meta:
        indexes = [models.Index(fields=["database_id"])]
