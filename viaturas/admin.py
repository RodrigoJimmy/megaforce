from django.contrib import admin

from .models import Marca, Modelo, Viatura

admin.AdminSite.site_header = "MegaForce"
admin.AdminSite.site_title = "MegaForce site admin"


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    pass


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca')
    list_select_related = ('marca',)


@admin.register(Viatura)
class ViaturaAdmin(admin.ModelAdmin):
    list_display = ('prefixo', 'modelo', 'status', 'placa', 'updated_at')
    list_display_links = ('prefixo', 'placa')
    list_filter = ('status', 'modelo', 'updated_at')
    search_fields = ('prefixo', 'placa')
    list_select_related = ('modelo',)

