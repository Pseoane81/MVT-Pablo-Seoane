from django.http import HttpResponse
from django.shortcuts import render
from famila.models import Familia
from django.template import loader


# Create your views here.
def familia(request):
    familia = Familia.objects.all()
    datos = {"datos":familia}
    plantilla = loader.get_template("home.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)