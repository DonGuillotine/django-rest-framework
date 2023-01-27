from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from product.models import ProductModel
from product.serializers import ProductSerializer

@api_view(['POST'])
def api_view(request):
    # To view error messages
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response(serializer.data)