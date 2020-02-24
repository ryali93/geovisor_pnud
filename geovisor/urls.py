from django.conf.urls import url, include
from django.urls import path, re_path
from dashboard.views import visor_html, dashboard, ChartTimeSerie



urlpatterns = [
    re_path(r'^.*\.html', visor_html, name='visor'),
    path('', dashboard, name='index'),
    url(r'^api/chart/data2/$', ChartTimeSerie.as_view(), name='api-chart-data'),
]
