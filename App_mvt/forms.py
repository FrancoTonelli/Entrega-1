from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    email = forms.EmailField()

class CoinFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    ticker = forms.CharField(max_length=10)
    precio = forms.IntegerField()

class OperacionFormulario(forms.Form):
    tipo = forms.CharField(max_length=15)
    activo = forms.CharField(max_length=20)
    precio = forms.IntegerField()
    cantidad = forms.IntegerField()
    fecha = forms.DateField()

class ClienteBusquedaFormulario(forms.Form):
    nombre = forms.CharField()

class CoinBusquedaFormulario(forms.Form):
    ticker = forms.CharField()

class OperacionBusquedaFormulario(forms.Form):
    activo = forms.CharField()
