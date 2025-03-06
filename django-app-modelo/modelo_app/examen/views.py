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

def createEvento(request):
    data = {}
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            fecha_inicio = request.POST.get('fecha_inicio')
            fecha_fin = request.POST.get('fecha_fin')
            localidad = request.POST.get('localidad')

            evento = Evento(name=name, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, localidad=localidad)
            evento.save()
            data["evento"] = evento 
            data["message"] = "Evento Creado"
            data["status"] = "success"
    except Exception as e:
        data["message"] = str(e)
        data["status"] = "error"

    return render(request, 'examen/eventosCreate.html', data)

def createBoleto(request):
    data = {}
    try:
        if request.method == 'POST':
            precio = request.POST.get('precio')
            localidad = request.POST.get('localidad')
            tipo_boleto = request.POST.get('tipo_boleto')
            evento = request.POST.get('evento')
            fecha = request.POST.get('fecha')

            boleto = Boleto(precio=precio, localidad=localidad, tipo_boleto=tipo_boleto, evento=evento, fecha=fecha)
            boleto.save()
            data["boleto"] = boleto 
            data["message"] = "Boleto Creado"
            data["status"] = "success"
    except Exception as e:
        data["message"] = str(e)
        data["status"] = "error"

    return render(request, 'examen/boletosCreate.html', data)