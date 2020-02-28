from rest_framework import serializers
from dashboard.models import tb_data_monthly

class tb_data_monthly_serializer(serializers.ModelSerializer):
    class Meta:
        model = tb_data_monthly
        fields = ('id', 'cod_est', 'data', 'pisco')
