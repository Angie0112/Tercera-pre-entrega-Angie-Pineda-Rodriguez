from django.shortcuts import render, redirect
from django.urls import reverse
def llenar_formulario(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

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

    url_exitosa = reverse('formulario')  # estudios/cursos/
    return redirect(url_exitosa)  
    
    else:  # GET
    formulario = CursoFormulario()
    http_response = render(
    request=request,
    template_name='entrega/formulario.html',
    context={'formulario': formulario}
   )
    return http_response

