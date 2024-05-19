from django.shortcuts import render

def pagina_principal(request):
    return render(request, "TransPorto/index.html")

from .models import Usuarios

def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'template.html', {'usuarios': usuarios})
