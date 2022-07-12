
from rest_framework import generics, mixins, authentication, permissions

from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import GenericAPIView

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
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductUpdateList(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class CreateListProduct(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DetailUpdateProduct(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, reqeust, *args, **kwargs):
        return serlf.partial_update(reqeust, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# class ProductListAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
