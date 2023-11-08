from  django.contrib import admin 
from django.urls import investigar_datos,crear-curso
from .views import *
urlpatterns = [
path("formulario/",llenar_formulario, name="llenar_formulario"),
path("cursos/", crear-formulario, name="crear_formulario"),
]