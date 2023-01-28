from rest_framework import generics
from .models import ProductModel
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # For a serializer for a user
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


# Another way of using class based views
# product_detail = ProductDetailAPIView.as_view();