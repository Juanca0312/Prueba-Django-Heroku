from pydoc import describe
from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=12)
    descripcion = models.TextField(max_length=100)
    precio = models.DecimalField(decimal_places=2, max_digits=7)