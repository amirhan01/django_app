from django.shortcuts import render
from product.models import Product
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def get_product(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

    