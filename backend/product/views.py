from rest_framework import generics
from .models import ProductModel
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # For a serializer for a user
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


# class ProductListAPIView(generics.ListAPIView):
#     queryset = ProductModel.objects.all()
#     serializer_class = ProductSerializer


# Using Function Based Views For Create, Retrieve or List
@api_view(['GET', 'POST'])
def product_alternate_view(request, pk=None):
    method = request.method
    if method == 'GET':
        if pk is not None:
            # The detail view with id i.e api/products/1
            obj = get_object_or_404(ProductModel, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # The List View for listing all items
        queryset = ProductModel.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
                # Save first before returning serializer.data
            serializer.save(content=content)
            return Response(serializer.data)




# Another way of using class based views
# product_detail = ProductDetailAPIView.as_view();