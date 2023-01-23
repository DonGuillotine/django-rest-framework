import json
from django.http import JsonResponse
from product.models import ProductModel

def api_view(request):
    model_instance = ProductModel.objects.all().order_by('?').first()
    data = {}
    if model_instance:
        data['id'] = model_instance.id
        data['title'] = model_instance.title
        data['content'] = model_instance.content
        data['price'] = model_instance.price
    return JsonResponse(data)