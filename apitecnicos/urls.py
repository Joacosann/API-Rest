from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/usuarios', UsuarioViewSet, 'apitecnicos-usuarios')
router.register('api/sucursales', SucursalViewSet, 'apitecnicos-sucursales')

# ---------------------- VEHICULO ----------------------------- #
router.register('api/vehiculos', VehicleViewSet, 'apitecnicos-vehiculos')
router.register('api/modelos', ModelViewSet, 'apitecnicos-modelos')
router.register('api/papeleos', PaperworkViewSet, 'apitecnicos-papeleos')

""" router.register('api/direcciones', DireccionViewSet, 'apitecnicos-direcciones')
router.register('api/contactos', ContactoViewSet, 'apitecnicos-contactos') """


urlpatterns = router.urls