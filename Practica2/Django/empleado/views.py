from django.shortcuts import render,get_object_or_404,redirect
import empleado
from empleado.models import Empleado
from empleado.forms import EmpleadoForm
from empleado.models import Departamento
from empleado.forms import DepartamentoForm
from empleado.models import JefeDepartamento
from empleado.forms import JefeDepartamentoForm
from empleado.models import Dept_empl
from empleado.forms import Dept_EmplForm

def detalleEmpleado(request,id):
    empleado = get_object_or_404(Empleado,pk=id)
    return render(request,'detalle.html',{'empleado':empleado})

def nuevoEmpleado(request):
    if request.method == 'POST':
        formaEmpleado = EmpleadoForm(request.POST)
        if formaEmpleado.is_valid():
            formaEmpleado.save()
            return redirect('index')
    else:
        formaEmpleado = EmpleadoForm()
        return render(request,'agregar.html',{'formaEmpleado':formaEmpleado})

def editarEmpleado(request,id):
    empleado = get_object_or_404(Empleado,pk=id)
    if request.method=='POST':
        formaEmpleado = EmpleadoForm(request.POST,instance=empleado)
        if formaEmpleado.is_valid():
            formaEmpleado.save()
            return redirect('index')
    else:
        formaEmpleado = EmpleadoForm(instance=empleado)
        return render(request,'editar.html',{'formaEmpleado':formaEmpleado})

def eliminarEmpleado(request,id):
    empleado = get_object_or_404(Empleado,pk=id)
    if empleado:
        empleado.delete()
    return redirect('index')

def detalleDepartamento(request,id):
    departamento = get_object_or_404(Departamento,pk=id)
    return render(request,'detalle_dept.html',{'departamento':departamento})

def nuevoDepartamento(request):
    if request.method == 'POST':
        formaDepartamento = DepartamentoForm(request.POST)
        if formaDepartamento.is_valid():
            formaDepartamento.save()
            return redirect('indexdep')
    else:
        formaDepartamento = DepartamentoForm()
        return render(request,'agregardept.html',{'formaDepartamento':formaDepartamento})

def editarDepartamento(request,id):
    departamento = get_object_or_404(Departamento,pk=id)
    if request.method=='POST':
        formaDepartamento = DepartamentoForm(request.POST,instance=departamento)
        if formaDepartamento.is_valid():
            formaDepartamento.save()
            return redirect('indexdep')
    else:
        formaDepartamento = DepartamentoForm(instance=departamento)
        return render(request,'editardpt.html',{'formaDepartamento':formaDepartamento})

def eliminarDepartamento(request,id):
    departamento = get_object_or_404(Departamento,pk=id)
    if departamento:
        departamento.delete()
    return redirect('indexdep')

def detalleJefeDepartamento(request,id):
    jefeDepartamento = get_object_or_404(JefeDepartamento,pk=id)
    return render(request,'detalle_jefedept.html',{'jefeDepartamento':jefeDepartamento})

def nuevoJefeDepartamento(request):
    if request.method == 'POST':
        formaJefeDepartamento = JefeDepartamentoForm(request.POST)
        if formaJefeDepartamento.is_valid():
            formaJefeDepartamento.save()
            return redirect('indexjefe')
    else:
        formaJefeDepartamento = JefeDepartamentoForm()
        return render(request,'agregar_jefedept.html',{'formaJefeDepartamento':formaJefeDepartamento})

def editarJefeDepartamento(request,id):
    jefeDepartamento = get_object_or_404(JefeDepartamento,pk=id)
    if request.method=='POST':
        formaJefeDepartamento = JefeDepartamentoForm(request.POST,instance=jefeDepartamento)
        if formaJefeDepartamento.is_valid():
            formaJefeDepartamento.save()
            return redirect('indexjefe')
    else:
        formaJefeDepartamento = JefeDepartamentoForm(instance=jefeDepartamento)
        return render(request,'editar_jefedpt.html',{'formaJefeDepartamento':formaJefeDepartamento})

def eliminarJefeDepartamento(request,id):
    jefeDepartamento = get_object_or_404(JefeDepartamento,pk=id)
    if jefeDepartamento:
        jefeDepartamento.delete()
    return redirect('indexjefe')

def detalleDept_Empl(request,id):
    dept_empl = get_object_or_404(Dept_empl,pk=id)
    return render(request,'detalle_dept_empl.html',{'dept_empl':dept_empl})

def nuevoDept_Empl(request):
    if request.method == 'POST':
        formaDept_Empl = Dept_EmplForm(request.POST)
        if formaDept_Empl.is_valid():
            formaDept_Empl.save()
            return redirect('indexdept_empl')
    else:
        formaDept_Empl = Dept_EmplForm()
        return render(request,'agregar_dept_empl.html',{'formaDept_Empl':formaDept_Empl})

def editarDept_empl(request,id):
    dept_empl = get_object_or_404(Dept_empl,pk=id)
    if request.method=='POST':
        formaDept_Empl = Dept_EmplForm(request.POST,instance=dept_empl)
        if formaDept_Empl.is_valid():
            formaDept_Empl.save()
            return redirect('indexdept_empl')
    else:
        formaDept_Empl = Dept_EmplForm(instance=dept_empl)
        return render(request,'editardept_empl.html',{'formaDept_Empl':formaDept_Empl})

def eliminarDept_Empl(request,id):
    dept_empl = get_object_or_404(Dept_empl,pk=id)
    if dept_empl:
        dept_empl.delete()
    return redirect('indexdept_empl')