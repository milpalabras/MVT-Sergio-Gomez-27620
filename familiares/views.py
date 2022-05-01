from django.shortcuts import render
from django.http import request
from familiares.models import persona

# Create your views here.


def vistafamiliares (request):
    
    familiares = persona.objects.all()

    return render (request, 'home.html', {'familiares': familiares} )
