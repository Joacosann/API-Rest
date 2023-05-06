from django.db import models


# Create your models here.
class Tecnico(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    dni = models.CharField(max_length=10) 
    nombre_usuario = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)
    status = models.CharField(max_length=10)
    branch = models.CharField(max_length=4)
    id_contacto = models.IntegerField()
    id_direccion = models.IntegerField()
    categoria = models.CharField(max_length=1)
    
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

