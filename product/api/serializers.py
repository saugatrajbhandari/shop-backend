from rest_framework import serializers
from product.models import  Product

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['_id', 'name', 'category', 'user', 'image', 'brand', 'price', 'description', 'countInStock', 'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')

        
