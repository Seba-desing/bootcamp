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
    return render (request,'listado_vehiculos.html',datos)


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


def form_update_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente = id)
    datos = {
        'form':VehiculoForm(instance = vehiculo)
    }
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST, instance = vehiculo )
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= "Modificado correctamente"
            datos['form'] = formulario

    return render (request,'form_update.html',datos)



def form_delete_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente = id)
    vehiculo.delete()
    return redirect(to="home") 