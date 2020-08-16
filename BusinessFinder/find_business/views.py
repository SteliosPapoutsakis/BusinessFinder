from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader

from .models import CompanyTypes, Company, Activity


def index(request):
    return render(request, 'find_business/index.html')
# Create your views here.

def business_query(request):
    '''
    returns result from client side query
    '''

    if request.method == 'POST':
        print(request.POST)
        data = {"test": "hello"}
        return JsonResponse(data)
    else:
        raise Http404()
