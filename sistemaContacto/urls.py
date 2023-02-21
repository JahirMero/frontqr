"""sistemaContacto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from Aplicaciones.qr import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.qr.urls')),
    #path('signup/', views.signup, name='signup'), #registro
    #path('signout/', views.signout, name='signout'), # cerrar sesion
    #path('signin/', views.signin, name='signin'), # login

]

"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', include('Aplicaciones.qr.urls'))
]

handler404 = 'Aplicaciones.qr.views.error_404_view'
"""