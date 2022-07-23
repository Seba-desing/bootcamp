from dataclasses import fields
from rest_framework import serializers
from app1.models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [ "idCategoria", "nombreCategoria"]

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = [ "idSucursal", "nombre", "region", "comuna","direccion" ]