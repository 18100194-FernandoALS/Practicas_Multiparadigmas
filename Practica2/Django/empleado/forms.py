from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm,EmailInput
from empleado.models import Departamento, Empleado,JefeDepartamento,Dept_empl

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        
class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class JefeDepartamentoForm(ModelForm):
    class Meta:
        model = JefeDepartamento
        fields = '__all__'

class Dept_EmplForm(ModelForm):
    class Meta:
        model = Dept_empl
        fields = '__all__'