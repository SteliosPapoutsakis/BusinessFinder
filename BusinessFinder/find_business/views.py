from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.template import loader



def index(request):
    return render(request, 'find_business/index.html')
# Create your views here.

def business_query(request):
    data = {"test": "hello"}
    return JsonResponse(data)
