from django.db import models
from cliente.models import Cliente
from pelicula.models import Copias
# Create your models here.
class Prestamo(models.Model):
    fecha_prestamo = models.DateField()
    fecha_entrega = models.DateField(null=True)
    idCliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL,null=True)
    idCopia = models.ForeignKey(Copias,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return f'{self.idCliente} pidio {self.idCopia} el dia {self.fecha_prestamo}'