from Producto_ms.models.Producto import Producto
from Producto_ms.serializers.productoSerializer import ProductoSerializer
from rest_framework import generics       

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer