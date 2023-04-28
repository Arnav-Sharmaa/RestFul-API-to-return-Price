from django.shortcuts import render
from django.http import JsonResponse
from .scraper import get_latest_price
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import elementSerializer
from .models import element
@api_view(['GET'])
def get_price(request):
    price = get_latest_price()
    if not element.objects.exists():
        element.objects.create(name=price[0],price=price[1])
    if element.objects.get(name=price[0]).price != price[1] :
        element.objects.filter(name=price[0]).update(price=price[1])
    updated_model=element.objects.get(name=price[0])
    serializer=elementSerializer(updated_model)
    return Response(serializer.data)

def home(request):
    return render(request, 'index.html')