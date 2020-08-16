from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from find_business.models import Company
from django.db.models import Q

def index(request):
    return render(request, 'find_business/index.html')
# Create your views here.

def business_query(request):
    '''
    returns result from client side query
    '''

    if request.method == 'POST':
        print(request.POST)
        query_dict = {}
        for company_attr in ('type','title','lat','lon','within'):
            val = request.POST.get(company_attr)
            if val:
                query_dict[company_attr] = val
                
        #companies = Company.objects.filter(query_dict)
        #companies = Company.objects.filter(Q(name))
        #companies = Company.

        return JsonResponse('')
    else:
        raise Http404()
