from django.shortcuts import render
from .serializers import RetailShopSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import RetailShop, Product


@api_view(['GET'])
def stores_list_view(request):
    shops = RetailShop.objects.all()
    serializer = RetailShopSerializer(shops, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def stores_detail_view(request, id):
    details = RetailShop.objects.get(id=id)
    serializer_stores = RetailShopSerializer(details, many=False)
    products = Product.objects.filter(related_shop=id)
    serializer_products = ProductSerializer(products, many=True)
    serializer_list = [serializer_stores.data, serializer_products.data]
    return Response(serializer_list)


@api_view(['POST'])
def add_product_view(request, id):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(related_shop=[id])
    return Response({"Added": "Product object was added"})