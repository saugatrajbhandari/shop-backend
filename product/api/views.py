from rest_framework.generics import (ListAPIView, RetrieveAPIView)
from .serializers import ProductSerializer
from product.models import Product

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = '_id'