from django.db import models

from django.db import models

class Kota (models.Model):
    id_kota = models.AutoField(primary_key=True)
    nama_kota = models.CharField(max_length=30)

    def __str__(self):
        return self.nama_kota
    
class Distrik (models.Model):
    id_distrik = models.AutoField(primary_key=True)
    kota = models.ForeignKey(Kota, on_delete=models.CASCADE)
    nama_distrik = models.CharField(max_length=30)

    def __str__(self):
        return self.nama_distrik