from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *

def llenar_formulario(request):
    
    if request.method == "POST":
        formulario = Formulario_Investigar(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data  
            nombre = data["nombre_completo"]
            correo = data["correo"]
            mensaje = data["mensaje"]
            tipo_de_contacto= data["tipo_de_contacto"]
            suscripción= data["suscripción"]
            informacion = investigar(
                nombre_completo=nombre, 
                correo=correo,
                mensaje=mensaje,
                tipo_de_contacto=tipo_de_contacto,
                suscripción=suscripción)
            informacion.save()  
            return redirect("mostrar_información")

    
    else:  

        formulario = Formulario_Investigar()
        
        http_response = render(
        request=request,
        template_name='formularios/formulario.html',
        context={'formulario': formulario} )

        return http_response
    
def mostrar_información(request):
    base_datos= investigar.objects.all()
    http_response = render(
        request=request,
        template_name='listados/data.html',
        context={'listados':base_datos} )
    return http_response

def buscar_informacion(request):
    
    if request.method == "POST":
       
        filtro = request.POST["busqueda"]

       
        busqueda = investigar.objects.filter(nombre_completo__icontains=filtro)

        
        http_response = render(
            request=request,
            template_name='listados/listado_filtrados.html',
            context={'busqueda': busqueda}
        )

        return http_response

    else:  
        http_response = render(
            request=request,
            template_name='formularios/formulario_busqueda.html',
            context={}
        )

        return http_response 

def crear_usuario(request):
        
    if request.method == "POST":
        formulario = Formulario_Investigar(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data  
            usuario = data["usuario"]
            contraseña = data["contraseña"]
            informacion = investigar(
                usuario=usuario, 
                contraseña=contraseña,
                )
            informacion.save()  
            return redirect("mostrar_información")

    else:  

        formulario = Formulario_Investigar()
        
        http_response = render(
        request=request,
        template_name='formularios/login.html',
        context={'formulario': formulario} )

        return http_response

def crear_detalles(request):
        
    if request.method == "POST":
        formulario = Formulario_Investigar(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data  
            compra = data["compra"]
            detalles_envio= data["detalles_envio"]
            informacion = investigar(
                compra=compra, 
                detalles_envio=detalles_envio,
                )
            informacion.save()  
            return redirect("mostrar_información")

    else:  

        formulario = Formulario_Investigar()
        
        http_response = render(
        request=request,
        template_name='formularios/detalles.html',
        context={'formulario': formulario} )

        return http_response


