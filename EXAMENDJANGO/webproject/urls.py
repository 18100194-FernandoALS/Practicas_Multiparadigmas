"""webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from webapp.views import bienvenido,bienvenido1, bienvenido2,bienvenido3
from cliente.views import detalle,eliminar,nueva,editar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenido,name='index'),
    path('cliente/',bienvenido1,name='indexcliente'),
    path('pelicula/',bienvenido2,name='indexpelicula'),
    path('prestamo/',bienvenido3,name='indexprestamo'),

    path('cliente/detalle_cliente/<int:id>',detalle),
    path('cliente/nuevo_cliente/',nueva),
    path('cliente/editar_cliente/<int:id>',editar),
    path('cliente/eliminar_cliente/<int:id>',eliminar),
]
