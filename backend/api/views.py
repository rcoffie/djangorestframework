from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# def api_home(request, *args, **kwargs):
#
#     return JsonResponse({"message":" Hi there, this is your Django API response "})

#
# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id','title','price'])
#
#     # return JsonResponse(data)
#     return Response(data)


# @api_view(["POST"])
# def api_home(request, *args, **kwargs):
#
#     # data = request.data
#     # instance = Product.objects.all().order_by("?").first()
#     # data = {}
#     # if instance:
#     #     data = ProductSerialzier(instance).data
#     serializer =  ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         print(serializer.data)
#         return Response(serializer.data)


@api_view(['GET'])
def api_home(request):
    return Response({"message":"Hellow for today! see you tommorow"})
