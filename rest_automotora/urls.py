from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sucursal', SucursalViewset)

urlpatterns = [
    path("lista_categoria/", lista_categoria, name="lista categoria"),
    path("lista_sucursal/", lista_sucursal, name="lista sucursal"),
    path("", include(router.urls)),
]
