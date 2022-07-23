from tkinter import CASCADE
from django.db import models

# Create your models here.
class Sucursal(models.Model):
    idSucursal = models.IntegerField(primary_key=True, verbose_name="Id sucursal")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    region = models.CharField(max_length=50, verbose_name="Region")
    comuna = models.CharField(max_length=50, verbose_name="Comuna")
    direccion = models.CharField(max_length=50, verbose_name="Dirección")

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="id categoria")
    nombreCategoria = models.CharField(max_length=20, verbose_name="nombre")

    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, primary_key=True, verbose_name="patente")
    marca = models.CharField(max_length=30, verbose_name="marca")
    modelo = models.CharField(max_length=30, verbose_name="modelo")
    color = models.CharField(max_length=50, verbose_name="color")
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo

class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True, verbose_name="id cliente")
    nombre = models.CharField(max_length=50, verbose_name="Nombre cliente")

    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    idVendedor = models.IntegerField(primary_key=True, verbose_name="id cliente")
    nombre = models.CharField(max_length=50, verbose_name="Nombre vendedor")
    run = models.CharField(max_length=15, verbose_name="run")
    cantidadVentas = models.IntegerField(verbose_name="Cantidad de ventas")

    def __str__(self):
        return self.nombre
