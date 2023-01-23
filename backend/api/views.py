from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from product.models import ProductModel
from product.serializers import ProductSerializer

@api_view(['POST'])
def api_view(request):
    instance = ProductModel.objects.all().order_by('?').first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        # data = model_to_dict(instance, fields=['id', 'title'])
    return Response(data)