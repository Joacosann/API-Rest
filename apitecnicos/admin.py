from django.contrib import admin
from .models import *

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre_completo', 'dni', 'nombre_usuario', 'contrasena',
    'tipo','branch', 'id_contacto', 'id_direccion', 'categoria')

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id_sucursal','nombre','calle','altura','localidad','provincia','cod_postal')


# ---------------------- VEHICULO ----------------------------- #
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('g08_id', 'g08_model_id', 'g08_paperwork_id', 'g08_plate', 'g08_purchase_price',
    'g08_sell_price','g08_status', 'g08_technical_score', 'g08_branch', 'g08_kilometers', 'g08_message', 'g08_combustion_type')

class ModelAdmin(admin.ModelAdmin):
    list_display = ('g06_id','g06_brand','g06_model','g06_year','g06_base_price','g06_origin')

class PaperworkAdmin(admin.ModelAdmin):
    list_display = ('g07_id','g07_faults_debt','g07_vpa','g07_rva','g07_vtv')

""" class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id_direccion','calle','ciudad','estado','codigo_postal','pais','altura')

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id_contacto','email','codigo_telefono','numero_telefono') """

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Sucursal,SucursalAdmin)

# ---------------------- VEHICULO ----------------------------- #
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Model,ModelAdmin)
admin.site.register(Paperwork,PaperworkAdmin)

""" admin.site.register(Direccion,DireccionAdmin)
admin.site.register(Contacto,ContactoAdmin) """