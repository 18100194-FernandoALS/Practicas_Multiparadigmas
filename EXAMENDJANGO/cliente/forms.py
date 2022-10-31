from django.forms import ModelForm,EmailInput
from cliente.models import Cliente
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }