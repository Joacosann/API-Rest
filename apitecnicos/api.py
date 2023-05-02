from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

class TecnicoViewSet(viewsets.ModelViewSet):
    # Conjunto de datos
    queryset = Tecnico.objects.all()
    # Clases que tienen permiso de consulta
    permission_classes = [permissions.AllowAny]
    serializer_class = TecnicoSerializer

class TallerViewSet(viewsets.ModelViewSet):
    # Conjunto de datos
    queryset = Taller.objects.all()
    # Clases que tienen permiso de consulta
    permission_classes = [permissions.AllowAny]
    serializer_class = TallerSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    # Conjunto de datos
    queryset = Sucursal.objects.all()
    # Clases que tienen permiso de consulta
    permission_classes = [permissions.AllowAny]
    serializer_class = SucursalSerializer
    
class DireccionViewSet(viewsets.ModelViewSet):
    # Conjunto de datos
    queryset = Direccion.objects.all()
    # Clases que tienen permiso de consulta
    permission_classes = [permissions.AllowAny]
    serializer_class = DireccionSerializer