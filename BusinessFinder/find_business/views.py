from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader

from django.db.models import Q

from .models import CompanyTypes, Company

COORDINATE_TO_MILES = 75.0

def index(request):
    companies = Company.objects.all()
    companies_dict = {
        'companies': companies
    }
    return render(request, 'find_business/index.html', companies_dict)
# Create your views here.

def business_query(request):
    '''
    returns result from client side query
    '''
    print(request)
    if request.method == 'POST':
        print(request.POST)
        query_dict = {}
        valid_dict = {}
        for company_attr in ('type','search','lat','lon','within'):
            val = request.POST.get(company_attr)
        
            if val:
                valid_dict[company_attr] = True
                query_dict[company_attr] = val
            else:
                valid_dict[company_attr] = False
        companies = Company.objects.all()
        print('a')
        if (valid_dict['search']):
            companies = Company.objects.filter(
                Q(name__contains=query_dict['search']) |
                Q(description__contains=query_dict['search'])
            )
        print('b')
        if (valid_dict['type']):
            mytype = CompanyTypes[query_dict['type']]
            companies = companies.filter(type=mytype)
        print('c')
        if (valid_dict['within'] & (query_dict['within'] != 0)):
            print('d')
            dist = float(query_dict['within'])/COORDINATE_TO_MILES
            lat = float(query_dict['lat'])
            lon = float(query_dict['lon'])
            lat_max = lat + dist
            lat_min = lat - dist
            lon_max = lon + dist
            lon_min = lon - dist
            print('e')
            companies = companies.filter(
                (Q(coordinatesLat__lte=lat_max) |
                Q(coordinatesLat__gte=lat_min)) &
                (Q(coordinatesLat__lte=lon_max) |
                Q(coordinatesLat__gte=lon_min)))

        print(companies.all())

        companies_dict = {
            'companies': companies.all()
        }

        return render(request, 'find_business/businesses_list.html', companies_dict)

    else:
        raise Http404()
