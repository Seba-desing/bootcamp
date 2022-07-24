from django import forms
from .models import Categoria, Sucursal, Vehiculo
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo', 'color','Categoria']
