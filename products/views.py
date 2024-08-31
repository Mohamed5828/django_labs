from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def product(request):
    return render(request , "products/product.html" )
    

@api_view(['GET','POST'])
def products(request):
    if request.method=='GET':
        products = Product.objects.all()
        print(products)
        ser = ProductSerializer(products,many=True)
        return Response(ser.data)
    elif request.method=='POST':
        ser = ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    # return render(request , "products/products.html" )

