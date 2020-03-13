from django.conf import settings
from django.db import models
from django.shortcuts import render
from django.contrib.gis.db import models as geomodels

# class tb_stations_pp(models.Model):
#     id = models.BigIntegerField(blank=False, null=False, primary_key=True)
#     pisco = models.FloatField(db_column='pisco', blank=True, null=True)
#     data = models.FloatField(db_column='data', blank=True, null=True)
#     mes = models.DateField(db_column='mes', blank=True, null=True)
#     cod_est = models.TextField(db_column='COD_EST', blank=True, null=True)
#
#     def __str__(self):
#         return self.cod_est
#
#     class Meta:
#         managed = False
#         db_table = 'tb_data_monthly'

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
