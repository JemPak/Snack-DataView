from django.db import models

class Product (models.Model):
    id_producto = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    cantidad = models.IntegerField(default=0)
    price = models.BigIntegerField(blank=False, null=True)
    description = models.TextField(max_length=2000, null=True)
    url_image = models.URLField(max_length=2000, blank=False, null=True)