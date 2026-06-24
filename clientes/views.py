from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from .models import Cliente
from .forms import ClienteForm


@login_required
@permission_required('clientes.view_cliente', raise_exception=True)
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})


@login_required
@permission_required('clientes.add_cliente', raise_exception=True)
def crear_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Cliente creado correctamente")
        return redirect('lista_clientes')

    return render(request, 'clientes/crear.html', {'form': form})


@login_required
@permission_required('clientes.change_cliente', raise_exception=True)
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        messages.success(request, "Cliente actualizado correctamente")
        return redirect('lista_clientes')

    return render(request, 'clientes/editar.html', {'form': form})


@login_required
@permission_required('clientes.delete_cliente', raise_exception=True)
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        cliente.delete()
        messages.success(request, "Cliente eliminado correctamente")
        return redirect('lista_clientes')

    return render(request, 'clientes/eliminar.html', {'cliente': cliente})