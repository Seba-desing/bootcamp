from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name = "home"),
    path("registro/", registro, name = "registro"),
    path('form', form, name="form")
]
