from rest_framework import serializers
from Producto_ms.models.Producto import Producto



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto','nombre','cantidad','precio','descripcion']