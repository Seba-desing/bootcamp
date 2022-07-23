from pstats import Stats
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app1.models import *
from .serializers import *

@csrf_exempt
@api_view(['GET','POST'])
def lista_categoria(request):

    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','POST'])
def lista_sucursal(request):

    if request.method == 'GET':
        sucursal = Sucursal.objects.all()
        serializer = SucursalSerializer(sucursal, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SucursalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SucursalViewset(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
# Create your views here.
