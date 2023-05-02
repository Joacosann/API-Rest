from django.db import models

# Create your models here.
class Tecnico(models.Model):
    id_empleado = models.CharField(max_length=4, primary_key=True)
    dni = models.CharField(max_length=8) 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    categoria = models.CharField(max_length=1)
    contrasena = models.CharField(max_length=20)
    id_taller = models.CharField(max_length=4)
    
class Taller(models.Model):
    id_taller = models.CharField(max_length=4)
    nombre = models.CharField(max_length=20)
    id_direccion = models.CharField(max_length=20)
    id_sucursal = models.CharField(max_length=20)
    mail =models.CharField(max_length=20)
    
class Sucursal(models.Model):
    id_sucursal = models.CharField(max_length=4)
    nombre = models.CharField(max_length=20)
    id_direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    
class Direccion(models.Model):
    id_direccion = models.CharField(max_length=4)
    calle = models.CharField(max_length=40)
    altura = models.CharField(max_length=5)
    provincia = models.CharField(max_length=40)
    pais = models.CharField(max_length=25)

