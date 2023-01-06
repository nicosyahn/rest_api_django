from rest_framework import serializers
from ..models import Kota, Distrik

class KotaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Kota
        fields = ('id_kota', 'nama_kota')

class DistrikSerializers(serializers.ModelSerializer):

    class Meta:
        model = Distrik
        fields = ('id_distrik', 'kota', 'nama_distrik')