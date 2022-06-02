from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    #path("familia", views.familia),
    path("alumnos", views.alumnos, name="alumnos"),
    path("cursos", views.cursos, name="cursos"),
    path("profesores", views.profesores, name="profesores"),
    path("alta_alumno", views.alta_alumno, name="alta_alumno"),
    path("alta_profesor", views.alta_profesor, name="alta_profesor"),
    path("alta_curso", views.alta_curso, name="alta_curso"),
    path("busqueda", views.busqueda, name="busqueda"),
    path("res_busqueda", views.res_busqueda),
]