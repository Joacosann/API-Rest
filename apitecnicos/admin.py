from django.contrib import admin
from .models import *

# Register your models here.
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre_completo', 'dni', 'nombre_usuario', 'categoria', 'contrasena',
    'tipo', 'status', 'branch', 'id_contacto', 'id_direccion', 'categoria')

class TallerAdmin(admin.ModelAdmin):
    list_display = ('id_taller','nombre','id_direccion','id_sucursal','mail')

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id_sucursal','nombre','id_direccion','telefono')

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id_direccion','calle','altura','provincia','pais')

admin.site.register(Tecnico,TecnicoAdmin)
admin.site.register(Taller,TallerAdmin)
admin.site.register(Sucursal,SucursalAdmin)
admin.site.register(Direccion,DireccionAdmin)