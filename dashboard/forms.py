from django import forms
from .models import tb_stations_pp


class DataMonthlyForm(forms.ModelForm):
    class Meta:
        model = tb_stations_pp
        fields = ['cod_est', 'mes', 'pisco', 'data']