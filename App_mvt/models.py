from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()

class Coin(models.Model):
    nombre = models.CharField(max_length=20)
    ticker = models.CharField(max_length=10)
    precio = models.IntegerField()

class Operacion(models.Model):
    tipo = models.CharField(max_length=15)
    activo = models.CharField(max_length=20)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    fecha = models.DateField()

