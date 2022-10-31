from django.shortcuts import render
from cliente.models import Cliente
from prestamo.models import Prestamo
from pelicula.models import Copias
# Create your views here.
def bienvenido(request):
    return render(request,'index.html')
def bienvenido1(request):
    clientes = Cliente.objects.order_by('id')
    return render(request,'cliente.html',{'clientes':clientes})
def bienvenido2(request):
    copias = Copias.objects.order_by('id')
    return render(request,'pelicula.html',{'copias':copias})
def bienvenido3(request):
    prestamos = Prestamo.objects.order_by('id')
    return render(request,'prestamo.html',{'prestamos':prestamos})