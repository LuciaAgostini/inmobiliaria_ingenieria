from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login
from .forms import RegistroUsuarioForm


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save()

            # Asignar automáticamente el grupo "Clientes"
            try:
                grupo = Group.objects.get(name='Clientes')
                usuario.groups.add(grupo)
            except Group.DoesNotExist:
                pass

            login(request, usuario)
            return redirect('home')

    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro.html', {'form': form})