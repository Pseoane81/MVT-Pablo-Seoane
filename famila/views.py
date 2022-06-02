from django.http import HttpResponse
from django.shortcuts import redirect, render
from famila.models import Familia,Alumno,Profesor,Curso
from django.template import loader
from famila.forms import Formulario_Listo


# Create your views here.

def inicio(request):
    return render(request, "padre.html")

def alumnos(request):
    alum = Alumno.objects.all()
    datos = {"datos":alum}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)

def profesores(request):
    prof = Profesor.objects.all()
    datos = {"datos":prof}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)

def cursos(request):
    curso = Curso.objects.all()
    datos = {"datos":curso}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)

def alta_alumno(request):

    if request.method == "POST":
        #mi_formulario = Formulario_Listo(request.POST)
        #if mi_formulario.is_valid():
            #data= mi_formulario.cleaned_data
            persona= Alumno(nombre=request.POST["nombre"],camada=request.POST["camada"],Fecha_Nac=request.POST["fecha"])
            persona.save()
            return redirect("alumnos")

    return render(request, "alta_alumno.html")

def alta_curso(request):
    
    if request.method == "POST":
        #mi_formulario = Formulario_Listo(request.POST)
        #if mi_formulario.is_valid():
            #data= mi_formulario.cleaned_data
            curso= Curso(nombre=request.POST["nombre"],camada=request.POST["camada"])
            curso.save()
            return redirect("cursos")

    return render(request, "alta_curso.html")

def alta_profesor(request):
    
    if request.method == "POST":
        #mi_formulario = Formulario_Listo(request.POST)
        #if mi_formulario.is_valid():
            #data= mi_formulario.cleaned_data
            profesor= Profesor(nombre=request.POST["nombre"],Apellido=request.POST["Apellido"],Especialidad=request.POST["especialidad"],mail=request.POST["mail"])
            profesor.save()
            return redirect("profesores")

    return render(request, "alta_profesor.html")
    

def busqueda(request):

    return render(request, "buscarcurso.html")


def res_busqueda(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        alumno= Alumno.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html", {"alumno": alumno})
    else:
        return HttpResponse("Campo Vacio")

    

    
