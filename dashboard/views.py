from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import tb_data_monthly
from .forms import DataMonthlyForm

from rest_framework.response import Response
from rest_framework.views import APIView

def dashboard(request):
    return render(request, "app/index.html", {})
#
# def dashboard(request):
#     context = {}
#     template = loader.get_template('app/index.html')
#     return HttpResponse(template.render(context, request))

def index(request):
    context = {}
    return render(request, 'app/index.html', context)

# def visor_html(request):
#     context = {}
#     load_template = request.path.split('/')[-1]
#     template = loader.get_template('app/' + load_template)
#     return HttpResponse(template.render(context, request))

def list_stations(request):
    datos = []
    print(datos)
    for dato in tb_data_monthly.objects.all():
        datos.append(dato.cod_est)
    datos = list(set(datos))
    print(datos)
    context = {
        'estaciones_list': datos
    }
    return render(request, "app/list_station.html", context)

def actualizar_grafico(request, codigo):
    unique_note = get_object_or_404(tb_data_monthly, id=codigo)
    form = DataMonthlyForm(request.POST or None, request.FILES or None, instance=unique_note)
    if form.is_valid():
        form.instance.user = request.cod_est
        return redirect('/app/list')

    context = {
        'form': form
    }
    return render(request, "app/create.html", context)


class ChartTimeSerie(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data_pisco = dict()
        data_estacion = dict()
        for station in tb_data_monthly.objects.all():
            if station.pisco > 0:
                if station.cod_est == "X114050":
                    data_pisco[station.mes] = station.pisco
                    data_estacion[station.mes] = station.data
        data_pisco = dict(data_pisco)

        data = {
            "pisco_labels": data_pisco.keys(),
            "pisco_data": data_pisco.values(),
            "estacion_data": data_estacion.values()
        }
        return Response(data)
