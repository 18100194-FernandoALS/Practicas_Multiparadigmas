
from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    año = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f'Pelicula {self.id}: {self.titulo}'

class Copias(models.Model):
    num_copias = models.IntegerField()
    formato = models.CharField(max_length=255)
    pelicula = models.ForeignKey(Pelicula,on_delete = models.SET_NULL,null=True)

    def __str__(self) -> str:
        return f'Copia de {self.pelicula.titulo}'