from rest_framework import serializers
from dashboard.models import tb_stations_pp

class tb_data_monthly_serializer(serializers.ModelSerializer):
    class Meta:
        model = tb_stations_pp
        fields = ('id', 'cod_est', 'data', 'pisco')
