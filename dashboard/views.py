from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import Http404

# from .models import tb_stations_pp
from .models import gpo_cuencas_tdps, data_bh_month, data_bh_historic, data_hydrogram_month, data_hydrogram_year

from rest_framework.response import Response
from rest_framework.views import APIView

from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.defaults import page_not_found


def view_404(request, exception):
    return render(request, 'app/404.html')

def base(request):
    context = {}
    return render(request, 'app/index.html', context)

def listar_database(request):
    context = {}
    return render(request, 'app/list_database.html', context)

def listar_mapas(request):
    context = {}
    return render(request, 'app/list_mapas.html', context)

def listar_cuencas(request):
    list_cuenca = []
    a = 0
    for cuenca in gpo_cuencas_tdps.objects.all():
        if 'Intercuenca' not in cuenca.nombre:
            a += 1
            list_cuenca.append({
                'orden': a,
                'codigo': cuenca.codigo,
                'nombre': cuenca.nombre,
                'area': round(cuenca.area, 2),
                'geom': cuenca.geom
            })
    context = {
        'cuencas_list': list_cuenca
    }
    return render(request, 'app/list_cuencas.html', context)

# def listar_estaciones(request):
#     cod_est = []
#     nom_est = []
#     for dato in tb_stations_pp.objects.all():
#         cod_est.append(dato.cod_est)
#         nom_est.append(dato.cod_est)
#     cod_est = list(set(cod_est))
#     context = {
#         'estaciones_list': cod_est
#     }
#     return render(request, 'app/list_station.html', context)

def mapa(request):
    context = {}
    return render(request, 'app/mapa.html', context)

# class EstacionPISCO_Details(APIView):
#     def get_object(self, pk):
#         try:
#             data_total = tb_stations_pp.objects.all()
#             data_estacion = dict()
#             data_pisco = dict()
#             for station in data_total:
#                 if station.cod_est == pk:
#                     data_pisco[station.mes] = station.pisco
#                     data_estacion[station.mes] = station.data
#             data_pisco = dict(data_pisco)
#             data = {
#                 "pisco_labels": data_pisco.keys(),
#                 "pisco_data": data_pisco.values(),
#                 "estacion_data": data_estacion.values()
#             }
#             return data
#         except tb_stations_pp.DoesNotExist:
#             raise Http404
#     def get(self, request, pk, format=None):
#         data = self.get_object(pk)
#         return Response(data)


def grafico(request, codigo):
    context = {'codigo': codigo}
    return render(request, 'app/dash.html', context)

def cuenca(request, codigo):
    # Datos del balance hidrico
    geo_json = extract_geom_cuenca(codigo)
    bh_monthly = extract_data_bh_monthly(codigo)
    bh_historico = extract_data_bh_historic(codigo)
    tb_monthly = {}
    tb_historico = {}
    hydrograph_month = extract_hydrograph_month(codigo)
    hydrograph_year = extract_hydrograph_year(codigo)

    context = {
        'geometria': geo_json,
        'bh_monthly': bh_monthly,
        'bh_historico': bh_historico,
        'tb_monthly': tb_monthly,
        'tb_historico': tb_historico,
        'hydrograph_month': hydrograph_month,
        'hydrograph_year': hydrograph_year
    }
    return render(request, "app/cuenca.html", context)

def extract_geom_cuenca(codigo):
    from django.core.serializers import serialize
    print(gpo_cuencas_tdps.objects.filter(codigo=codigo))
    geometria = serialize('geojson', gpo_cuencas_tdps.objects.filter(codigo=codigo),
                          geometry_field='geom',
                          fields=('codigo', 'nombre'))
    import json
    geom_json = json.loads(geometria)
    # coords = []
    # for g in geom_json['features'][0]["geometry"]["coordinates"][0][0]:
    #     y = g[0]
    #     x = g[1]
    #     coords.append([x, y])
    # geom_json['features'][0]["geometry"]["coordinates"][0][0] = coords
    geo_json = {
        "type": "Feature",
        "name": "nombre",
        "properties": {},
        "geometry": geom_json['features'][0]["geometry"]
    }
    return geo_json

def extract_data_bh_monthly(codigo):
    datos = data_bh_month.objects.filter(cod_cuenca=codigo)
    data = {
        'pp': [d.pp for d in datos],
        'etr': [d.etr for d in datos],
        'runoff': [d.escurr for d in datos]
    }
    return data

def extract_data_bh_historic(codigo):
    datos = data_bh_historic.objects.filter(cod_cuenca=codigo)
    data = {
        'pp': [d.pp for d in datos],
        'etr': [d.etr for d in datos],
        'runoff': [d.escurr for d in datos]
    }
    return data

def extract_hydrograph_month(codigo):
    datos = data_hydrogram_month.objects.filter(cod_cuenca=codigo)
    data = [d.caudal for d in datos]
    return data

def extract_hydrograph_year(codigo):
    import datetime, time
    datos = data_hydrogram_year.objects.filter(cod_cuenca=codigo)
    data = [[int(round(d.mes.timestamp() * 1000)), d.caudal] for d in datos]
    return data
