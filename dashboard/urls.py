from django.urls import path, re_path
from .views import dashboard, actualizar_grafico, list_stations, index
from django.conf.urls import url, include

app_name = 'app'

urlpatterns = [
    # re_path(r'^.*\.html', visor_html, name='visor'),
    path('index/', index, name='index'),
    path('list_station/', list_stations, name='list_station'),
    path('update_graph/', actualizar_grafico, name='update_graph'),
]
