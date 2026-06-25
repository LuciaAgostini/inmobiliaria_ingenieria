from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre", required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError("Ese nombre de usuario ya existe")

        return username