from django.contrib import admin
from empleado.models import Empleado,Departamento,JefeDepartamento,Dept_empl
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Departamento)
admin.site.register(JefeDepartamento)
admin.site.register(Dept_empl)