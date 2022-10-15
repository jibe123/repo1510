from rest_framework import serializers

from .models import RetailShop, Product


class RetailShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailShop
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
