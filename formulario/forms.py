from django import forms
from .models import *

class Formulario_Investigar(forms.ModelForm):

    class Meta:

        model = investigar
        fields = "__all__"