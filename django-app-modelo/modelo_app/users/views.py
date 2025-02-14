from django.shortcuts import render
from .models import users

def indexUsers(request):

    Users = users.objects.all()
    data = {
        "users": Users,
        "titulo": "Lista de Clientes"
            }

    return render(request, 'users/index.html', data)

