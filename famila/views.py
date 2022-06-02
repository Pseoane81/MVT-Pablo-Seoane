from django.http import HttpResponse
from django.shortcuts import redirect, render
from famila.models import Familia
from django.template import loader
from famila.forms import Formulario_Listo


# Create your views here.

def inicio(request):
    return render(request, "home.html")

def padre(request):
    return render(request, "padre.html")

def alumnos(request):
    return render(request, "alumnos.html")

def contactos(request):
    return render(request, "contactos.html")

def formulario(request):

    if request.method == "POST":
        #mi_formulario = Formulario_Listo(request.POST)
        #if mi_formulario.is_valid():
            #data= mi_formulario.cleaned_data
            persona= Familia(nombre=request.POST["nombre"],edad=request.POST["edad"],Fecha_Nac=request.POST["fecha"])
            persona.save()
            return redirect("cursos")

    return render(request, "formulario.html")
    

    
def cursos(request):
    familia = Familia.objects.all()
    datos = {"datos":familia}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)