from django.contrib import admin
from .models import Propiedad, TipoPropiedad, Operacion


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'tipo', 'operacion')
    search_fields = ('titulo', 'direccion')
    list_filter = ('tipo', 'operacion')
    ordering = ('titulo',)


admin.site.register(TipoPropiedad)
admin.site.register(Operacion)