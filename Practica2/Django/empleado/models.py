
from email.policy import default
from random import choices
from django.db import models

class Empleado(models.Model):
    fecha_nacimiento = models.DateField()
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    generos = [('F','Femenino'),('M','Masculino')]
    genero = models.CharField(max_length=1,choices=generos,default='F')
    fecha_contratacion = models.DateField()

    def __str__(self) -> str:
        return f'Empleado {self.id}: {self.nombre} {self.apellido}'

class Departamento(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Departamento {self.id}: {self.nombre}'

class JefeDepartamento(models.Model):
    idDepartamento = models.ForeignKey(Departamento,on_delete = models.CASCADE,null=True)
    idEmpleado = models.ForeignKey(Empleado,on_delete = models.SET_NULL,null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self) -> str:
        return f'JefeDepartamento {self.id}: {self.idEmpleado.nombre} {self.idEmpleado.apellido}'

class Dept_empl(models.Model):
    idEmpleado = models.ForeignKey(Empleado,on_delete = models.SET_NULL,null=True)
    idDepartamento = models.ForeignKey(Departamento,on_delete = models.SET_NULL,null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    def __str__(self) -> str:
        return f'{self.idEmpleado} en {self.idDepartamento}'