from django.shortcuts import render, get_object_or_404, redirect
from .models import users

def indexUsers(request):

    Users = users.objects.all()
    data = {
        "users": Users,
        "titulo": "Lista de Clientes"
            }

    return render(request, 'users/index.html', data)

def createUserView(request):
    return render(request, 'users/create.html')

def createUser(request):
    data = {}
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            age = request.POST.get('age')
            rfc = request.POST.get('rfc')
            photo = request.POST.get('photo')

            user = users(name=name, email=email, age=age, rfc=rfc, photo=photo)
            user.save()
            data["user"] = user
            data["message"] = "User Created"
            data["status"] = "success"
    except Exception as e:
            
        data["message"] = str(e)
        data["status"] = "error"

    return render(request, 'users/create.html', data)

def userDetail(request, id):
    user = get_object_or_404(users, id=id)  # Obtener el usuario o mostrar 404

    if request.method == "POST":
        # Solo actualizar los campos permitidos
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.rfc = request.POST.get('rfc')

        # Guardar los cambios en la base de datos
        user.save()

        return redirect('userDetail', id=user.id)  # Redirigir al detalle del usuario actualizado

    return render(request, 'users/detail.html', {"user": user})        
