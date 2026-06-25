from django.urls import path
from .views import (
    home,
    lista_propiedades,
    crear_propiedad,
    editar_propiedad,
    eliminar_propiedad,
    atencion
)

urlpatterns = [
    path('', home, name='home'),
    path('propiedades/', lista_propiedades, name='lista_propiedades'),
    path('propiedades/crear/', crear_propiedad, name='crear_propiedad'),
    path('propiedades/editar/<int:pk>/', editar_propiedad, name='editar_propiedad'),
    path('propiedades/eliminar/<int:pk>/', eliminar_propiedad, name='eliminar_propiedad'),
    path('atencion/', atencion, name='atencion'),
]