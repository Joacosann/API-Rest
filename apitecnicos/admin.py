from django.contrib import admin
from .models import *

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre_completo', 'dni', 'nombre_usuario', 'contrasena',
    'tipo','branch', 'id_contacto', 'id_direccion', 'categoria')

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id_sucursal','nombre','id_direccion','telefono')

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id_direccion','calle','ciudad','estado','codigo_postal','pais','altura')

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id_contacto','email','codigo_telefono','numero_telefono')

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Sucursal,SucursalAdmin)
admin.site.register(Direccion,DireccionAdmin)
admin.site.register(Contacto,ContactoAdmin)