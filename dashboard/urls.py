from django.urls import path, re_path
# from dashboard.views import visor_html, dashboard, actualizar_grafico, list_stations
from django.conf.urls import url, include, handler404

from dashboard.views import base, mapa, grafico, cuenca
# from dashboard.views import  listar_estaciones, EstacionPISCO_Details
from dashboard.views import  listar_database, listar_mapas, listar_cuencas

handler404 = 'dashboard.views.view_404'

app_name = 'app'

urlpatterns = [
    path('', base, name='base'),
    path('grafico/<str:codigo>/', grafico, name='grafico'),
    path('cuenca/<str:codigo>/', cuenca, name='cuenca'),

    path('list_database/', listar_database, name='listar_database'),
    path('list_mapas/', listar_mapas, name='listar_mapas'),
    path('list_cuencas/', listar_cuencas, name='listar_cuencas'),
    path('mapa/', mapa, name='mapa'),

]
