from apps.product.models import Product
from apps.product.serializers import ProductoSerializer
from rest_framework import generics       

class ProductListCreateView(generics.ListCreateAPIView): # create and get all products
    queryset = Product.objects.all()
    serializer_class = ProductoSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView): # retrieve all products
    serializer_class = ProductoSerializer
    queryset = Product.objects.all()
