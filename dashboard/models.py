from django.conf import settings
from django.db import models
from django.shortcuts import render
from django.contrib.gis.db import models as geomodels



class tb_data_monthly(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    pisco = models.FloatField(db_column='pisco', blank=True, null=True)
    data = models.FloatField(db_column='data', blank=True, null=True)
    mes = models.DateField(db_column='mes', blank=True, null=True)
    cod_est = models.TextField(db_column='COD_EST', blank=True, null=True)

    def __str__(self):
        return self.cod_est

    class Meta:
        managed = False
        db_table = 'tb_data_monthly'

class gpo_cuencas(geomodels.Model):
    id = geomodels.BigIntegerField(blank=False, null=False, primary_key=True)
    codigo = geomodels.TextField(db_column='codigo', blank=True, null=True)
    nombre = geomodels.TextField(db_column='nombre', blank=True, null=True)
    area = geomodels.FloatField(db_column='area_km2', blank=True, null=True)
    geom = geomodels.MultiPolygonField()

    def __str__(self):
        return self.codigo

    class Meta:
        managed = False
        db_table = 'gpo_cuencas_tdps'
