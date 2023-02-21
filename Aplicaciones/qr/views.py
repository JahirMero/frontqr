from django.shortcuts import render, redirect, get_object_or_404
from .models import user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def Inscripciones(request):
    return render(request, 'dashboard/form_basic.html')

@login_required
def crear_evento(request):
    return render(request, "dashboard/crear-event.html")

@login_required
def autent_qr(request):
    return render(request, "dashboard/autent_qr.html")

@login_required
def event_creado(request):
    return render(request, "dashboard/event_creado.html")

@login_required
def charts(request):
    return render(request, "dashboard/charts.html")



#### views de Inicio de sesion ####

# REGISTRO
def signup(request):
    if request.method == 'GET':
        print('if')
        return render(request, 'dashboard/authentication-register.html', {"form": UserCreationForm})
    else:
        print('else')
        if request.POST["password1"] == request.POST["password2"]:
            try:
                usuario = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('/')
            except IntegrityError:
                return render(request, 'dashboard/authentication-register.html', {
                    "form": UserCreationForm, 
                    "error": "Username already exists."})

        return render(request, 'dashboard/authentication-register.html', {
            "form": UserCreationForm, 
            "error": "Passwords did not match."})


# cerrrar sesion

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

# login

def signin(request):
    if request.method == 'GET':
        return render(request, 'dashboard/authentication-login.html', {"form": AuthenticationForm})
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'dashboard/authentication-login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, usuario)
        return redirect('/')




#error pagina no encontrada 
def error_404_view(request, exception):
    return render(request,'error_404.html')