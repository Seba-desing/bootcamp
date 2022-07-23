from django import forms
from .models import Categoria, Sucursal
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass