from .models import *
from rest_framework import viewsets,permissions
from .serializers import *

class UsuarioViewSet(viewsets.ModelViewSet):
    # Conjunto de datos
    queryset = Usuario.objects.all()
    # Clases que tienen permiso de consulta
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    # Conjunto de datos
    queryset = Sucursal.objects.all()
    # Clases que tienen permiso de consulta
    permission_classes = [permissions.AllowAny]
    serializer_class = SucursalSerializer
    
""" class DireccionViewSet(viewsets.ModelViewSet):
    # Conjunto de datos
    queryset = Direccion.objects.all()
    # Clases que tienen permiso de consulta
    permission_classes = [permissions.AllowAny]
    serializer_class = DireccionSerializer

class ContactoViewSet(viewsets.ModelViewSet):
    # Conjunto de datos
    queryset = Contacto.objects.all()
    # Clases que tienen permiso de consulta
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactoSerializer """