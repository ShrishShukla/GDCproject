from django.shortcuts import render
from django.http import HttpResponse
from .models import SensorData
from .serializers import SensorDataSerializer
from rest_framework import viewsets
from django_tables2 import SingleTableView
from .tables import SensorDataTable
from django.contrib.auth.decorators import login_required


class SensorDataListView(SingleTableView):
    model = SensorData
    table_class = SensorDataTable
    template_name = 'Linker/SensorData.html'


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


def home(request):
    
    return render(request, 'Linker/home.html')


def about(request):
	return render(request, 'Linker/about.html')

@login_required
def dash(request):
	context = {
        'posts': SensorData.objects.all()
    }
	return render(request, 'Linker/dashboard.html', context)

def f404(request):
	return render(request, 'Linker/404.html')