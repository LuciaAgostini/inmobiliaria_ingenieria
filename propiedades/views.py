from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from .models import Propiedad
from .forms import PropiedadForm


def home(request):
    return render(request, 'home.html')


@login_required
@permission_required('propiedades.view_propiedad', raise_exception=True)
def lista_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'propiedades/lista.html', {
        'propiedades': propiedades
    })


@login_required
@permission_required('propiedades.add_propiedad', raise_exception=True)
def crear_propiedad(request):
    form = PropiedadForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Propiedad creada correctamente.")
        return redirect('lista_propiedades')

    return render(request, 'propiedades/crear.html', {
        'form': form
    })


@login_required
@permission_required('propiedades.change_propiedad', raise_exception=True)
def editar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)

    form = PropiedadForm(request.POST or None, request.FILES or None, instance=propiedad)

    if form.is_valid():
        form.save()
        messages.success(request, "Propiedad actualizada correctamente.")
        return redirect('lista_propiedades')

    return render(request, 'propiedades/editar.html', {
        'form': form,
        'propiedad': propiedad
    })


@login_required
@permission_required('propiedades.delete_propiedad', raise_exception=True)
def eliminar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)

    if request.method == 'POST':
        propiedad.delete()
        messages.success(request, "Propiedad eliminada correctamente.")
        return redirect('lista_propiedades')

    return render(request, 'propiedades/eliminar.html', {
        'propiedad': propiedad
    })