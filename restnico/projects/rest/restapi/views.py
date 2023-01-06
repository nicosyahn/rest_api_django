from ..models import Kota, Distrik
from .serializer import KotaSerializers, DistrikSerializers
from rest_framework import viewsets, generics

class KotaViewset(viewsets.ModelViewSet):
    serializer_class = KotaSerializers
    queryset = Kota.objects.all()

class DistrikViewset(viewsets.ModelViewSet):
    serializer_class = DistrikSerializers
    queryset = Distrik.objects.all()
