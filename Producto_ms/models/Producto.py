from django.db import models

class Producto (models.Model):
    id_producto = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    cantidad = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    descripcion = models.TextField(max_length=2000, blank=True)