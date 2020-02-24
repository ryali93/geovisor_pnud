from django import forms
from .models import tb_data_monthly


class DataMonthlyForm(forms.ModelForm):
    class Meta:
        model = tb_data_monthly
        fields = ['cod_est', 'mes', 'pisco', 'data']