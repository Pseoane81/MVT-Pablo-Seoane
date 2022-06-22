from django import forms


class Formulario_Listo(forms.Form):
    nombre= forms.CharField(max_length=40)
    edad= forms.IntegerField()
    Fecha_Nac= forms.DateField()


class Formulario_Curso(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()