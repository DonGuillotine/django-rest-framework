from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from product.models import ProductModel
from product.serializers import ProductSerializer

@api_view(['POST'])
def api_view(request):
    data = request.data
    return Response(data)