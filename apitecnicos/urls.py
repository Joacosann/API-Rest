from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/tecnicos', TecnicoViewSet, 'apitecnicos-tecnicos')
router.register('api/direcciones', DireccionViewSet, 'apitecnicos-direcciones')
router.register('api/sucursales', SucursalViewSet, 'apitecnicos-sucursales')


urlpatterns = router.urls