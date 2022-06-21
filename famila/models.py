from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    Fecha_Nac = models.DateField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Fecha Nacimiento: {self.Fecha_Nac}"

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    Fecha_Nac = models.DateField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada} - Fecha Nacimiento: {self.Fecha_Nac}"
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Especialidad = models.CharField(max_length=40)
    mail = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.Apellido} - Especialidad: {self.Especialidad} - Mail: {self.mail}"
