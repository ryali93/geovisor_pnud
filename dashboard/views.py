from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import Http404
from django.conf import settings

# from .models import tb_stations_pp
from .models import gpo_cuencas_tdps, gpo_subcuencas_tdps, data_bh_month, data_bh_historic, data_hydrogram_month, data_hydrogram_year

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'app/404.html', data)

def base(request):
    context = {}
    return render(request, 'app/index.html', context)

def contact(request):
    return render(request, 'app/contact.html', {})

def listar_database(request):
    context = {}
    return render(request, 'app/list_database.html', context)

def listar_mapas(request):
    context = {}
    return render(request, 'app/list_mapas.html', context)

def mapas_cuencas(request, codigo):
    context = {'codigo': codigo}
    return render(request, 'app/mapas_cuencas.html', context)

def mapas_subcuencas(request, codigo):
    context = {'codigo': codigo}
    return render(request, 'app/mapas_subcuencas.html', context)

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


def listar_subcuencas(request):
    list_subcuenca = []
    a = 0
    for cuenca in gpo_subcuencas_tdps.objects.all().order_by('nom_parent'):
        a += 1
        list_subcuenca.append({
            'orden': a,
            'codigo': cuenca.codigo,
            'nombre': cuenca.nombre,
            'cod_parent': cuenca.cod_parent,
            'nom_parent': cuenca.nom_parent,
            'area': round(cuenca.area, 2),
            'geom': cuenca.geom
        })
    context = {
        'subcuencas_list': list_subcuenca
    }
    return render(request, 'app/list_subcuencas.html', context)

def mapa(request):
    context = {}
    return render(request, 'app/mapa.html', context)

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

def subcuenca(request, codigo):
    # Datos del balance hidrico
    geo_json, geo_parent_json = extract_geom_subcuenca(codigo)
    bh_monthly = extract_data_bh_monthly(codigo)
    bh_historico = extract_data_bh_historic(codigo)
    tb_monthly = {}
    tb_historico = {}
    hydrograph_month = extract_hydrograph_month(codigo)
    hydrograph_year = extract_hydrograph_year(codigo)

    context = {
        'geometria': geo_json,
        'geometria_parent': geo_parent_json,
        'bh_monthly': bh_monthly,
        'bh_historico': bh_historico,
        'tb_monthly': tb_monthly,
        'tb_historico': tb_historico,
        'hydrograph_month': hydrograph_month,
        'hydrograph_year': hydrograph_year
    }
    return render(request, "app/subcuenca.html", context)

def extract_geom_cuenca(codigo):
    import json
    try:
        geometria = gpo_cuencas_tdps.objects.filter(codigo=codigo)
        geom_json = json.loads(geometria[0].geom)
    except:
        geom_json = []
    geo_json = {
        "type": "Feature",
        "name": "nombre",
        "properties": {},
        "geometry": geom_json
    }
    return geo_json

def extract_geom_subcuenca(codigo):
    import json
    try:
        geometria = gpo_subcuencas_tdps.objects.filter(codigo=codigo)
        cod_parent = geometria[0].cod_parent
        geometria_parent = gpo_cuencas_tdps.objects.filter(codigo=cod_parent)
        geom_json = json.loads(geometria[0].geom)
        geom_parent_json = json.loads(geometria_parent[0].geom)
    except:
        geom_json = []
        geom_parent_json = []
    geo_json = {
        "type": "Feature",
        "name": "nombre",
        "properties": {},
        "geometry": geom_json
    }
    geo_parent_json = {
        "type": "Feature",
        "name": "nombre",
        "properties": {},
        "geometry": geom_parent_json
    }
    return geo_json, geo_parent_json


def extract_data_bh_monthly(codigo):
    try:
        datos = data_bh_month.objects.filter(cod_cuenca=codigo)
        data = {
            'pp': [d.pp for d in datos],
            'etr': [d.etr for d in datos],
            'runoff': [d.escurr for d in datos]
        }
    except:
        data = {'pp':[], 'etr':[],'runoff':[]}
    return data

def extract_data_bh_historic(codigo):
    try:
        datos = data_bh_historic.objects.filter(cod_cuenca=codigo)
        data = {
            'pp': [d.pp for d in datos],
            'etr': [d.etr for d in datos],
            'runoff': [d.escurr for d in datos]
        }
    except:
        data = {'pp':[], 'etr':[],'runoff':[]}
    return data

def extract_hydrograph_month(codigo):
    try:
        datos = data_hydrogram_month.objects.filter(cod_cuenca=codigo)
        data = [d.caudal for d in datos]
    except:
        data = []
    return data

def extract_hydrograph_year(codigo):
    try:
        datos = data_hydrogram_year.objects.filter(cod_cuenca=codigo)
        data = [[int(round(d.mes.timestamp() * 1000)), d.caudal] for d in datos]
    except:
        data = []
    return data


