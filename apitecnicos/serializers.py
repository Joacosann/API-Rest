from rest_framework import serializers
from .models import *

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('id_empleado','dni','nombre','apellido','categoria','contrasena','id_taller')
        read_only_fields = ('id_empleado','dni','nombre','apellido','categoria','contrasena','id_taller')

class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = ('id_taller','nombre','id_direccion','id_sucursal','mail')
        read_only_fields = ('id_taller','nombre','id_direccion','id_sucursal','mail')

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id_sucursal','nombre','id_direccion','telefono')
        read_only_fields = ('id_sucursal','nombre','id_direccion','telefono')

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('id_direccion','calle','altura','provincia','pais')
        read_only_fields = ('id_direccion','calle','altura','provincia','pais')