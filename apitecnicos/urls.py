from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/usuarios', UsuarioViewSet, 'apitecnicos-usuarios')
router.register('api/sucursales', SucursalViewSet, 'apitecnicos-sucursales')
""" router.register('api/direcciones', DireccionViewSet, 'apitecnicos-direcciones')
router.register('api/contactos', ContactoViewSet, 'apitecnicos-contactos') """


urlpatterns = router.urls