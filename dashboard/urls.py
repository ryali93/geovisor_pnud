from django.urls import path, re_path
from django.conf.urls import url, include
from django.conf.urls import handler404
from dashboard.views import base, mapa, grafico, cuenca, subcuenca, contact
from dashboard.views import  listar_database, listar_mapas, listar_cuencas, listar_subcuencas

from dashboard.views import mapas_cuencas, mapas_subcuencas

app_name = 'app'

urlpatterns = [
    path('', base, name='base'),
    path('grafico/<str:codigo>/', grafico, name='grafico'),
    path('subcuenca/<str:codigo>/', subcuenca, name='cuenca'),
    path('cuenca/<str:codigo>/', cuenca, name='cuenca'),
    path('list_database/', listar_database, name='listar_database'),
    path('list_mapas/', listar_mapas, name='listar_mapas'),
    path('list_cuencas/', listar_cuencas, name='listar_cuencas'),
    path('list_subcuencas/', listar_subcuencas, name='listar_subcuencas'),
    path('mapa/', mapa, name='mapa'),
    path('cuenca/<str:codigo>/mapas/', mapas_cuencas, name='mapas_cuencas'),
    path('subcuenca/<str:codigo>/mapas', mapas_subcuencas, name='mapas_subcuencas'),
    path('contact/', contact, name='contact'),
]
