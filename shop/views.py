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
    serializer = RetailShopSerializer(details, many=False)
    return Response(serializer.data)
