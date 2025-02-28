import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Boleto, Evento, Localidads, Producto, TipoBoleto

def indexExamen(request):
    boletos = Boleto.objects.all()
    eventos = Evento.objects.all()  
    data = {
        "boletos": boletos,  # Corregido: antes era "boleto"
        "eventos": eventos,  # Corregido: antes era "Eventos" (mayúscula)
        "titulo": "Lista de Boletos"
    }
    return render(request, 'examen/index.html', data)

def eventosExamen(request):
    eventos = Evento.objects.all()  
    data = {
        "eventos": eventos,  
        "titulo": "Lista de Eventos"
    }
    return render(request, 'examen/eventos.html', data) 

def boletosExamen(request):
    boletos = Boleto.objects.all()  
    data = {
        "boletos": boletos,  
        "titulo": "Lista de Boletos"
    }
    return render(request, 'examen/boletos.html', data)  #

def eventoExamen(request):
    evento = Evento.objects.all()  
    data = {
        "eventos": evento,  
        "titulo": "Lista de Eventos"
    }
    return render(request, 'examen/evento.html', data) 

def productosExamen(request):
    productos = Producto.objects.all()  
    data = {
        "productos": productos, 
        "titulo": "Lista de Productos"
    }
    return render(request, 'examen/productos.html', data)

# def productos(request):
#     localidad_id = request.GET.get('localidad_id')
#     if localidad_id:
#         productos = Producto.objects.filter(localidad_id=localidad_id)
#     else:
#         productos = Producto.objects.all()

#     return render(request, 'examen/productos.html', {'productos': productos})