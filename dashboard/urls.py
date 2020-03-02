from django.urls import path, re_path
# from dashboard.views import visor_html, dashboard, actualizar_grafico, list_stations
from django.conf.urls import url, include, handler404

from dashboard.views import base, listar_estaciones, mapa, grafico, listar_database, listar_mapas
from dashboard.views import EstacionPISCO_Details

handler404 = 'dashboard.views.view_404'

app_name = 'app'

urlpatterns = [
    path('', base, name='base'),
    path('grafico/<str:codigo>/', grafico, name='grafico'),
    path('list_database/', listar_database, name='listar_database'),
    path('list_estaciones/', listar_estaciones, name='listar_estaciones'),
    path('list_mapas/', listar_mapas, name='listar_mapas'),
    path('mapa/', mapa, name='mapa'),

    url(r'^api/chart/data_estacion/(?P<pk>.+)/$', EstacionPISCO_Details.as_view()),
]
