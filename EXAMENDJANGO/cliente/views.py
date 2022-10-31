from django.shortcuts import render,get_object_or_404,redirect
from cliente.models import Cliente
from cliente.forms import ClienteForm
# Create your views here.
def detalle(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    return render(request,'detallecliente.html',{'cliente':cliente})

def nueva(request):
    if request.method == 'POST':
        formaCliente = ClienteForm(request.POST)
        if formaCliente.is_valid():
            formaCliente.save()
            return redirect('indexcliente')
    else:
        formaPersona = ClienteForm()
        return render(request,'agregarcliente.html',{'formaCliente':formaPersona})

def editar(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    if request.method=='POST':
        formaCliente = ClienteForm(request.POST,instance=cliente)
        if formaCliente.is_valid():
            formaCliente.save()
            return redirect('indexcliente')
    else:
        formaCliente = ClienteForm(instance=cliente)
        return render(request,'editarcliente.html',{'formaCliente':formaCliente})

def eliminar(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    if cliente:
        cliente.delete()
    return redirect('indexcliente')