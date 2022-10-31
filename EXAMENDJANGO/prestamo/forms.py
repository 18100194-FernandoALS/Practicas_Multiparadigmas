from django.forms import ModelForm,EmailInput
from prestamo.models import Prestamo
class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'