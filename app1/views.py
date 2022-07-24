from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserCreationForm, VehiculoForm
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from .models import Vehiculo
# Create your views here.

def home(request):
    vehiculo = Vehiculo.objects.all()
    datos = {
            'Vehiculo':vehiculo
    }
    return render (request,'home.html',datos)


def registro(request):
    data = {
        'form': UserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data['username'], password= formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='home')
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)



def form(request):
    datos ={
        'form': VehiculoForm()
    }
    if request.method == 'POST':
        formulario  = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()

    return render (request, 'form_create.html',datos)
