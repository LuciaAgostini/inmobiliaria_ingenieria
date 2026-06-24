from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro(request):
    form = RegistroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'usuarios/registro.html', {'form': form})