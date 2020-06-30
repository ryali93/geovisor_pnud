from django.conf import settings
from django.db import models
from django.shortcuts import render
from django.contrib.gis.db import models as geomodels

class gpo_cuencas_tdps(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    codigo = models.TextField(db_column='codigo', blank=True, null=True)
    nombre = models.TextField(db_column='nombre', blank=True, null=True)
    area = models.FloatField(db_column='area_km2', blank=True, null=True)
    geom = models.TextField(db_column='geom_json', blank=True, null=True)

    def __str__(self):
        return self.codigo

    class Meta:
        managed = False
        db_table = 'gpo_cuencas_tdps'

class gpo_subcuencas_tdps(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    codigo = models.TextField(db_column='codigo', blank=True, null=True)
    nombre = models.TextField(db_column='nombre', blank=True, null=True)
    area = models.FloatField(db_column='area_km2', blank=True, null=True)
    cod_parent = models.TextField(db_column='cod_parent', blank=True, null=True)
    nom_parent = models.TextField(db_column='nom_parent', blank=True, null=True)
    geom = models.TextField(db_column='geom_json', blank=True, null=True)

    def __str__(self):
        return self.codigo

    class Meta:
        managed = False
        db_table = 'gpo_subcuencas_tdps'

class tb_subcuencas_tdps_resultados(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    codigo = models.TextField(db_column='codigo', blank=True, null=True)

    pp_month = models.TextField(db_column='pp_month', blank=True, null=True)
    etp_month = models.TextField(db_column='etp_month', blank=True, null=True)
    etr_month = models.TextField(db_column='etr_month', blank=True, null=True)
    q_month = models.TextField(db_column='q_month', blank=True, null=True)
    flow_out_month = models.TextField(db_column='flow_out_month', blank=True, null=True)
    # wyld_month = models.TextField(db_column='wyld_month', blank=True, null=True)
    # surq_month = models.TextField(db_column='surq_month', blank=True, null=True)

    pp_anual = models.TextField(db_column='pp_anual', blank=True, null=True)
    etp_anual = models.TextField(db_column='etp_anual', blank=True, null=True)
    etr_anual = models.TextField(db_column='etr_anual', blank=True, null=True)
    q_anual = models.TextField(db_column='q_anual', blank=True, null=True)
    flow_out_anual = models.TextField(db_column='flow_out_anual', blank=True, null=True)
    wyld_anual = models.TextField(db_column='wyld_anual', blank=True, null=True)
    # surq_anual = models.TextField(db_column='surq_anual', blank=True, null=True)

    pp_clima = models.TextField(db_column='pp_clima', blank=True, null=True)
    etp_clima = models.TextField(db_column='etp_clima', blank=True, null=True)
    etr_clima = models.TextField(db_column='etr_clima', blank=True, null=True)
    q_clima = models.TextField(db_column='q_clima', blank=True, null=True)
    flow_out_clima = models.TextField(db_column='flow_out_clima', blank=True, null=True)
    wyld_clima = models.TextField(db_column='wyld_clima', blank=True, null=True)
    # surq_clima = models.TextField(db_column='surq_clima', blank=True, null=True)

    def __str__(self):
        return self.codigo

    class Meta:
        managed = False
        db_table = 'tb_subcuencas_resultados'

class data_bh_month(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    cod_cuenca = models.TextField(db_column='cod_cuenca', blank=True, null=True)
    nom_cuenca = models.TextField(db_column='nom_cuenca', blank=True, null=True)
    mes = models.IntegerField(db_column='mes', blank=True, null=True)
    pp = models.FloatField(db_column='pp', blank=True, null=True)
    etp = models.FloatField(db_column='etp', blank=True, null=True)
    etr = models.FloatField(db_column='etr', blank=True, null=True)
    escurr = models.FloatField(db_column='escurr', blank=True, null=True)
    caudal = models.FloatField(db_column='caudal', blank=True, null=True)

    def __str__(self):
        return self.cod_cuenca

    class Meta:
        managed = False
        db_table = 'tb_bh_month'

class data_bh_historic(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    cod_cuenca = models.TextField(db_column='cod_cuenca', blank=True, null=True)
    nom_cuenca = models.TextField(db_column='nom_cuenca', blank=True, null=True)
    anno = models.IntegerField(db_column='anno', blank=True, null=True)
    pp = models.FloatField(db_column='pp', blank=True, null=True)
    etp = models.FloatField(db_column='etp', blank=True, null=True)
    etr = models.FloatField(db_column='etr', blank=True, null=True)
    escurr = models.FloatField(db_column='escurr', blank=True, null=True)
    caudal = models.FloatField(db_column='caudal', blank=True, null=True)

    def __str__(self):
        return self.cod_cuenca

    class Meta:
        managed = False
        db_table = 'tb_bh_historic'

class data_hydrogram_month(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    cod_cuenca = models.TextField(db_column='cod_cuenca', blank=True, null=True)
    nom_cuenca = models.TextField(db_column='nom_cuenca', blank=True, null=True)
    mes = models.IntegerField(db_column='mes', blank=True, null=True)
    caudal = models.FloatField(db_column='caudal', blank=True, null=True)

    def __str__(self):
        return self.cod_cuenca

    class Meta:
        managed = False
        db_table = 'tb_hydrogram_month'

class data_hydrogram_year(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    cod_cuenca = models.TextField(db_column='cod_cuenca', blank=True, null=True)
    nom_cuenca = models.TextField(db_column='nom_cuenca', blank=True, null=True)
    mes = models.DateTimeField(db_column='mes', blank=True, null=True)
    caudal = models.FloatField(db_column='caudal', blank=True, null=True)

    def __str__(self):
        return self.cod_cuenca

    class Meta:
        managed = False
        db_table = 'tb_hydrogram_year'
