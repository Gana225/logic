from django.http import JsonResponse, HttpResponse
from .models import FoodItem,Product
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .serializers import FoodItemsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
def menu_list(request):
    items = FoodItem.objects.all()
    data = [model_to_dict(item) for item in items]
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def food(request):
    queryset = FoodItem.objects.all()
    serializer = FoodItemsSerializer(queryset,many=True,context={"request": request})
    return Response(serializer.data,status=200)



@api_view(["POST","PATCH"])
def order(request):
    print(request.data)
    return Response(request.data)


def test(request):
    data = Product.objects.all()
    for i in data:
        print(i.image.url)
    return HttpResponse("HI hello")