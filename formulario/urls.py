from django.urls import path
from .views import *

urlpatterns = [
path("formulario/",llenar_formulario, name="llenar_formulario"),
path("acceder/",mostrar_información, name="mostrar_información"),
path("buscar/",buscar_informacion, name="buscar_informacion"),
path("buscar/",crear_usuario, name="crear_usuario"),
path("buscar/",crear_detalles, name="crear_detalles")]