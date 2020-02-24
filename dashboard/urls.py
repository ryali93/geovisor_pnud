from django.urls import path, re_path
from dashboard.views import visor_html, dashboard, actualizar_grafico, list_stations
from django.conf.urls import url, include

app_name = 'app'

urlpatterns = [
    re_path(r'^.*\.html', visor_html, name='visor'),
    path('', dashboard, name='index'),
    # path('<codigo>/update/', actualizar_grafico, name='update'),
    url('list_station/', list_stations, name='list_station'),
]
