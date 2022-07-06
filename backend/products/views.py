
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
# from django.http import Http404
from django.shortcuts import get_object_or_404


class ProductDetialAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #overwriting queryset with perform_create method

    # def perform_create(self, serializer):
    #     # print(serializer.validated_data)
    #     title = serializer.validated_data.get('title')
    #     content = serializer.validated_data.get('content')
    #     or None
    #     if content is None:
    #         content = title
    #     serializer.save(content=content)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# class ProductListAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProdutUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeletAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

def product_alt_view(request, *args, **kwargs):
    method = request.method

    if method == 'GET':
        pass

        qs = Product.objects

    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if srializer.is_valid(raise_exception=True):
            print(serializer.data)
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status=400)
