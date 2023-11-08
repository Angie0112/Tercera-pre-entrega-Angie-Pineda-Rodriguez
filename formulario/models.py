from django.db import models
options=[[0,"numero de celular"]
        [1,"correo"]                  ]

class investigar (models.Model):
    nombre_completo=models.CharField(max_length=100, verbose_name="Nombre y Apellido")
    correo=models.EmailField(verbose_name="correo electronico")
    mensaje=models.TextField(verbose_name="Mensaje")
    tipo_de_contacto=models.IntegerField(choises=options,verbose_name="tipo de contacto")
    suscripción=models.BooleanField(default=False,verbose_name="suscribirme a correos informativos")
def _str_ (self):
    return f"{self. nombre_completo},{self.correo}{self.correo}{self.mensaje}{self.tipo_de_contacto}"# Create your models here.
