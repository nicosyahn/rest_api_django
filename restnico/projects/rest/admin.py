from django.contrib import admin
from django.contrib import admin
from .models import Kota, Distrik

class tb_kota(admin.ModelAdmin):
    list_display = ('id_kota', 'nama_kota')
    list_display_links = ('id_kota', 'nama_kota')
    search_fields = ('nama_kota',)
    list_per_page = 5

class tb_distrik(admin.ModelAdmin):
    list_display = ('id_distrik', 'kota', 'nama_distrik')
    list_display_links = ('id_distrik', 'kota', 'nama_distrik')
    search_fields = ('nama_kota',)
    list_per_page = 5

admin.site.register(Kota, tb_kota)
admin.site.register(Distrik, tb_distrik)