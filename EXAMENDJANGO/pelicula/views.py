from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from pelicula.models import Copias
from pelicula.forms import CopiaForm
# Create your views here.
def detalle(request,id):
    cliente = get_object_or_404(Copias,pk=id)
    return render(request,'detalle.html',{'persona':cliente})

def nueva(request):
    if request.method == 'POST':
        formaCliente = CopiaForm(request.POST)
        if formaCliente.is_valid():
            formaCliente.save()
            return redirect('index')
    else:
        formaPersona = CopiaForm()
        return render(request,'agregar.html',{'formaPersona':formaPersona})

def editar(request,id):
    cliente = get_object_or_404(Copias,pk=id)
    if request.method=='POST':
        formaCliente = CopiaForm(request.POST,instance=cliente)
        if formaCliente.is_valid():
            formaCliente.save()
            return redirect('index')
    else:
        formaCliente = CopiaForm(instance=cliente)
        return render(request,'editar.html',{'formaPersona':formaCliente})

def eliminar(request,id):
    cliente = get_object_or_404(Copias,pk=id)
    if cliente:
        cliente.delete()
    return redirect('index')