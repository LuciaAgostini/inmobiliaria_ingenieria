from django.contrib import admin
from .models import Cliente, Visita


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'email')
    ordering = ('apellido',)


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'propiedad', 'fecha')
    search_fields = ('cliente__nombre', 'propiedad__titulo')
    ordering = ('-fecha',)