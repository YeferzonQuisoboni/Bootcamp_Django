from django.shortcuts import render
from django.http import HttpResponse
from .models import City

#import libreria de todos los paises

# Create your views here.
def index(request):
    cities = City.objects.all()

    return render(request, 'cities.html', {'cities':cities})