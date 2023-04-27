from django.shortcuts import render
from django.http import JsonResponse
from .scraper import get_latest_price
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_price(request):
    element = get_latest_price()
    response = {"Name":element[0],
                "latest_price": element[1]}
    return Response(response)
