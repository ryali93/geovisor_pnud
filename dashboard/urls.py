from django.urls import path, re_path
# from dashboard.views import visor_html, dashboard, actualizar_grafico, list_stations
from django.conf.urls import url, include, handler404

from dashboard.views import base, mapa, grafico, cuenca, subcuenca
# from dashboard.views import  listar_estaciones, EstacionPISCO_Details
from dashboard.views import  listar_database, listar_mapas, listar_cuencas, listar_subcuencas

handler404 = 'dashboard.views.view_404'

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

]
