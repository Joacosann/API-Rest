from django.db import models


# Create your models here.
""" class Contacto(models.Model):
    id_contacto = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=50, default=' ')
    codigo_telefono = models.CharField(max_length=10, blank=True)
    numero_telefono = models.CharField(max_length=20, blank=True)

class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True)
    calle = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    estado= models.CharField(max_length=20)
    codigo_postal = models.CharField(max_length=4)
    pais = models.CharField(max_length=25)
    altura = models.CharField(max_length=5) """

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, null=True, blank=True)
    calle = models.CharField(max_length=50, null=True, blank=True)
    altura = models.CharField(max_length=4, null=True, blank=True)
    localidad = models.CharField(max_length=50, null=True, blank=True)
    provincia = models.CharField(max_length=30, null=True, blank=True)
    cod_postal = models.IntegerField(null=True, blank=True)


class Usuario(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    dni = models.CharField(max_length=10)
    nombre_usuario = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)
    branch = models.CharField(max_length=10, null=True, blank=True)
    # Arreglar
    id_contacto = models.IntegerField()
    id_direccion = models.IntegerField()
    categoria = models.CharField(max_length=1, null=True, blank=True)

# ---------------------- VEHICULO ----------------------------- #
class Vehicle(models.Model):
    g08_id = models.IntegerField(primary_key=True)
    g08_model_id = models.IntegerField()
    g08_paperwork_id = models.IntegerField()
    g08_plate = models.CharField(max_length=10)
    g08_purchase_price = models.FloatField(null=True, blank=True)
    g08_sell_price = models.FloatField(null=True, blank=True)
    g08_status = models.CharField(max_length=40)
    g08_technical_score = models.FloatField(null=True, blank=True)
    g08_branch = models.CharField(max_length=10, null=True, blank=True)
    g08_kilometers = models.CharField(max_length=10)
    g08_message = models.CharField( null=True, blank=True)
    g08_combustion_type = models.CharField(max_length=40)


class Model(models.Model):
    g06_id = models.IntegerField(primary_key=True)
    g06_brand = models.CharField(max_length=20)
    g06_model = models.CharField(max_length=20)
    g06_year = models.CharField(max_length=4)
    g06_base_price = models.FloatField()
    g06_origin = models.CharField(max_length=30)


class Paperwork(models.Model):
    g07_id = models.IntegerField(primary_key=True)
    g07_faults_debt = models.FloatField(null=True, blank=True)
    g07_vpa = models.BooleanField(default=False)
    g07_rva = models.BooleanField(default=False)
    g07_vtv = models.BooleanField(default=False)






