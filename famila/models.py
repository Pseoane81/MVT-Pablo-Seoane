from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    Fecha_Nac = models.DateField()

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    Fecha_Nac = models.DateField()
