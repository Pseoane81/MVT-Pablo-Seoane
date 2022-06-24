from tkinter.messagebox import NO
from django.http import HttpResponse
from django.shortcuts import redirect, render
from famila.models import Familia,Alumno,Profesor,Curso, avatar
from django.template import loader
from famila.forms import Formulario_Listo, Formulario_Curso, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


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

@login_required
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

    
def deleteCurso(request, id):
    curso= Curso.objects.get(id=id)
    curso.delete()

    curso= Curso.objects.all()

    return render(request, "cursos.html", {"datos": curso})
    #return redirect("cursos")


def editar(request, id):
    curso= Curso.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Formulario_Curso(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre= datos["nombre"]
            curso.camada= datos["camada"]
            curso.save()
        
        curso= Curso.objects.all()
        return render(request, "cursos.html", {"datos": curso})
        #return redirect("cursos")
    else:
        mi_formulario = Formulario_Curso(initial={"curso":curso.nombre, "camada": curso.camada})
            
    return render(request, "editar_Curso.html", {"mi_formulario":mi_formulario, "curso":curso})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario,password=contra)

            if user is not None:
                login(request,user)
                avatares = avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html", {"url": avatares[0].image.url})

            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:
            return HttpResponse(f"Form Incorrecto {form}")
    
    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form":form})

@login_required
def editarperfil(request):
    usuario = request.user

    if request.method == "POST":
        miformulario = UserEditForm(request.POST)

        if miformulario.is_valid():
            informacion = miformulario.cleaned_data

            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()

            return render(request, "inicio.html")

    else:
        miformulario = UserEditForm(initial={"email":usuario.email})

    return render(request, "editar_perfil.html", {"miformulario":miformulario, "usuario":usuario})
