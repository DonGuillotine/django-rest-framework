from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ProductModel
        fields = ['title', 'content', 'price', 'sale_price', 'my_discount']

    # obj is the instance of the model. So all properties are available
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, ProductModel):
            return None
        return obj.get_discount()