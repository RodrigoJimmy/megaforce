from django.contrib import admin

from .models import Marca, Modelo, Viatura


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    pass


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca')


@admin.register(Viatura)
class ViaturaAdmin(admin.ModelAdmin):
    list_display = ('prefixo', 'modelo', 'status', 'placa', 'updated_at')
    list_filter = ('status', 'modelo', 'updated_at')
    search_fields = ('prefixo', 'placa')
