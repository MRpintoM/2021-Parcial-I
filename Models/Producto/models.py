from django.db import models

from Models.Categoria.models import Categoria
from Models.Marca.models import Marca


class Producto(models.Model):
    nombreproduc = models.CharField(max_length=75)
    vencimiento = models.DateField()
    nommarc = models.ForeignKey(Marca, max_length=75, blank=False, on_delete=models.CASCADE)
    nomcat = models.ForeignKey(Categoria, max_length=75, blank=False, on_delete=models.CASCADE)
