from django.shortcuts import render, redirect

from django.contrib.auth.models import Group

from .forms import RegistroUsuarioForm


def registro(request):

    if request.method == 'POST':

        form = RegistroUsuarioForm(
            request.POST
        )

        if form.is_valid():

            usuario = form.save()

            grupo_clientes = Group.objects.get(
                name='Clientes'
            )

            usuario.groups.add(
                grupo_clientes
            )

            return redirect(
                'login'
            )

    else:

        form = RegistroUsuarioForm()

    return render(
        request,
        'registration/registro.html',
        {'form': form}
    )