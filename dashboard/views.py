from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import Http404

from .models import tb_data_monthly

from rest_framework.response import Response
from rest_framework.views import APIView

def base(request):
    context = {}
    return render(request, 'app/index.html', context)

def listar_database(request):
    datos = []
    print(datos)
    for dato in tb_data_monthly.objects.all():
        datos.append(dato.cod_est)
    datos = list(set(datos))
    print(datos)
    context = {
        'estaciones_list': datos
    }
    return render(request, 'app/list_station.html', context)

def mapa(request):
    context = {}
    return render(request, 'app/mapa.html', context)

class EstacionPISCO_Details(APIView):
    def get_object(self, pk):
        try:
            data_total = tb_data_monthly.objects.all()
            data_estacion = dict()
            data_pisco = dict()
            for station in data_total:
                if station.cod_est == pk:
                    data_pisco[station.mes] = station.pisco
                    data_estacion[station.mes] = station.data
            data_pisco = dict(data_pisco)
            data = {
                "pisco_labels": data_pisco.keys(),
                "pisco_data": data_pisco.values(),
                "estacion_data": data_estacion.values()
            }
            return data
        except tb_data_monthly.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        return Response(data)


def grafico(request, codigo):
    context = {'codigo': codigo}
    return render(request, 'app/dash.html', context)
