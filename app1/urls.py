from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name = "home"),
    path("registro/", registro, name = "registro"),
    path('form', form, name="form"),
    path('form_update_vehiculo/<id>/', form_update_vehiculo, name="form_update_vehiculo"),
    path('form_delete_vehiculo/<id>/', form_delete_vehiculo, name="form_delete_vehiculo")
]
