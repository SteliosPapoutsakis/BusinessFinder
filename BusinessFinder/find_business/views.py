from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the businessFinder index.")
# Create your views here.
    
def business_query(request):
    data = {"test": "hello"}
    return JsonResponse(data)

