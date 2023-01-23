import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.forms.models import model_to_dict
from product.models import ProductModel

@api_view(['GET'])
def api_view(request):
    model_instance = ProductModel.objects.all().order_by('?').first()
    data = {}
    if model_instance:
        data = model_to_dict(model_instance, fields=['id', 'title'])
    return Response(data)