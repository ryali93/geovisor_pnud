from django.conf import settings
# from django.db import models
from django.shortcuts import render
# from django.contrib.gis.db import models as geomodels
# from djongo import models
from mongoengine import *
from geovisor.settings import DBNAME

connect(DBNAME)

class tb_stations_pp(Document):
    # id = BigIntegerField(blank=False, null=False, primary_key=True)
    pisco = FloatField(db_column='pisco', blank=True, null=True)
    data = FloatField(db_column='data', blank=True, null=True)
    mes = DateField(db_column='mes', blank=True, null=True)
    cod_est = StringField(db_column='COD_EST', blank=True, null=True)

    def __str__(self):
        return self.cod_est

    class Meta:
        managed = False
        db_table = 'tb_stations_pp'

class gpo_cuencas_tdps(Document):
    # id = BigIntegerField(blank=False, null=False, primary_key=True)
    codigo = StringField(db_column='codigo', blank=True, null=True)
    nombre = StringField(db_column='nombre', blank=True, null=True)
    area = FloatField(db_column='area_km2', blank=True, null=True)
    geom = MultiPolygonField(blank=True, null=True)

    def __str__(self):
        return self.codigo

    class Meta:
        managed = False
        db_table = 'gpo_cuencas_tdps'


class tb_bh_month(Document):
    # id = BigIntegerField(blank=False, null=False, primary_key=True)
    cod_cuenca = StringField(db_column='cod_cuenca', blank=True, null=True)
    nom_cuenca = StringField(db_column='nom_cuenca', blank=True, null=True)
    mes = LongField(db_column='mes', blank=True, null=True)
    pp = FloatField(db_column='pp', blank=True, null=True)
    etp = FloatField(db_column='etp', blank=True, null=True)
    etr = FloatField(db_column='etr', blank=True, null=True)
    escurr = FloatField(db_column='escurr', blank=True, null=True)
    caudal = FloatField(db_column='caudal', blank=True, null=True)

    def __str__(self):
        return self.cod_cuenca

    class Meta:
        managed = False
        db_table = 'tb_bh_month'

class tb_bh_historic(Document):
    # id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    cod_cuenca = StringField(db_column='cod_cuenca', blank=True, null=True)
    nom_cuenca = StringField(db_column='nom_cuenca', blank=True, null=True)
    anno = LongField(db_column='anno', blank=True, null=True)
    pp = FloatField(db_column='pp', blank=True, null=True)
    etp = FloatField(db_column='etp', blank=True, null=True)
    etr = FloatField(db_column='etr', blank=True, null=True)
    escurr = FloatField(db_column='escurr', blank=True, null=True)
    caudal = FloatField(db_column='caudal', blank=True, null=True)

    def __str__(self):
        return self.cod_cuenca

    class Meta:
        managed = False
        db_table = 'tb_bh_historic'

class tb_hydrogram_month(Document):
    # id = BigIntegerField(blank=False, null=False, primary_key=True)
    cod_cuenca = StringField(db_column='cod_cuenca', blank=True, null=True)
    nom_cuenca = StringField(db_column='nom_cuenca', blank=True, null=True)
    mes = LongField(db_column='mes', blank=True, null=True)
    caudal = FloatField(db_column='caudal', blank=True, null=True)

    def __str__(self):
        return self.cod_cuenca

    class Meta:
        managed = False
        db_table = 'tb_hydrogram_month'

class tb_hydrogram_year(Document):
    # id = BigIntegerField(blank=False, null=False, primary_key=True)
    cod_cuenca = StringField(db_column='cod_cuenca', blank=True, null=True)
    nom_cuenca = StringField(db_column='nom_cuenca', blank=True, null=True)
    mes = DateTimeField(db_column='mes', blank=True, null=True)
    caudal = FloatField(db_column='caudal', blank=True, null=True)

    def __str__(self):
        return self.cod_cuenca

    class Meta:
        managed = False
        db_table = 'tb_hydrogram_year'
