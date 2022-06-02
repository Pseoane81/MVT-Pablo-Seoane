from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    #path("familia", views.familia),
    path("padre", views.padre),
    path("alumnos", views.alumnos, name="alumnos"),
    path("contactos", views.contactos, name="contactos"),
    path("cursos", views.cursos, name="cursos"),
    path("formulario", views.formulario, name="formulario")
]