from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

# def api_home(request, *args, **kwargs):
#
#     return JsonResponse({"message":" Hi there, this is your Django API response "})


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','price'])

    # return JsonResponse(data)
    return Response(data)
