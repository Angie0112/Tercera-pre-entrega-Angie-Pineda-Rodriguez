from django import forms
from .models import *

class Formulario_Investigar(forms.ModelForm):

    class Meta:

        model = investigar
        fields = "__all__"

class Formulario_crear(forms.ModelForm):
    
    class Meta:

        model = crear
        fields = "__all__"

class Formulario_detallar(forms.ModelForm):
    
    class Meta:

        model = detallar
        fields = "__all__"