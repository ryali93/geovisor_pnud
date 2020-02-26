from django.conf.urls import url, include
from django.urls import path, re_path
from dashboard.views import dashboard, ChartTimeSerie
from django.contrib import admin



urlpatterns = [
    url(r'^', dashboard, name='dashboard'),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^api/chart/data2/$', ChartTimeSerie.as_view(), name='api-chart-data'),
]
