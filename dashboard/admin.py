from django.contrib import admin

# from .models import tb_stations_pp
from .models import gpo_cuencas_tdps, data_bh_month, data_bh_historic, data_hydrogram_month, data_hydrogram_year

# admin.site.register(tb_stations_pp)
admin.site.register(gpo_cuencas_tdps)
admin.site.register(data_bh_month)
admin.site.register(data_bh_historic)
admin.site.register(data_hydrogram_month)
admin.site.register(data_hydrogram_year)
