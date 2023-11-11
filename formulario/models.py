from django.db import models
options=[[0,"numero de celular"],
        [1,"correo"]                  ]

class investigar (models.Model):
    nombre_completo=models.CharField(max_length=100, verbose_name="Nombre y Apellido")
    correo=models.EmailField(verbose_name="correo electronico")
    mensaje=models.TextField(verbose_name="Mensaje")
    tipo_de_contacto=models.IntegerField(choices=options,verbose_name="tipo de contacto")
    suscripción=models.BooleanField(default=False,verbose_name="suscribirme a correos informativos")
def __str__ (self):
    return f"{self. nombre_completo},{self.correo}{self.correo}{self.mensaje}{self.tipo_de_contacto}"
class crear (models.Model):
    usuario=models.CharField(max_length=100, verbose_name="usuario")
    contraseña=models.CharField(max_length=100, verbose_name="contraseña")
    def __str__ (self):
        return f"{self. nombre_usuario},{self.contraseña}"
class detallar (models.Model):
    compra=models.CharField(max_length=100, verbose_name="compra")
    detalles_envio=models.TextField(verbose_name="Mensaje")
    def __str__ (self):
            return f"{self.compra},{self.detalles}"