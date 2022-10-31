from django.forms import ModelForm,EmailInput
from pelicula.models import Copia
class CopiaForm(ModelForm):
    class Meta:
        model = Copia
        fields = '__all__'
        