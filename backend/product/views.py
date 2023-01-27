from rest_framework import generics
from .models import ProductModel
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


# Another way of using class based views
# product_detail = ProductDetailAPIView.as_view();