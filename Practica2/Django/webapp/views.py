from django.shortcuts import render
from empleado.models import Departamento, Dept_empl, Empleado, JefeDepartamento
# Create your views here.

def bienvenido(request):
    empleados = Empleado.objects.order_by('id')
    return render(request,'bienvenido.html',{'empleados':empleados})
    #'empleados' debe ser el mismo nombre que en el html, donde el for
def bienvenido2(request):
    departamentos = Departamento.objects.order_by('id')
    return render(request,'departamentos.html',{'departamentos':departamentos})
def bienvenido3(request):
    jefe = JefeDepartamento.objects.order_by('id')
    return render(request,'jefedepartamento.html',{'jefes':jefe})
def bienvenido4(request):
    dept_empl = Dept_empl.objects.order_by('id')
    return render(request,'dept_empl.html',{'dept_empls':dept_empl})
