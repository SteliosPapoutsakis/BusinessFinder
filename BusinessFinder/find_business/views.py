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

    if request.method == 'POST':
        print(request.POST)
        query_dict = {}
        valid_dict = {}
        for company_attr in ('type','search','lat','lon','within'):
            val = request.POST.get(company_attr)
        
            if val:
                valid_dict[val] = True
                query_dict[company_attr] = val
            else:
                valid_dict[val] = False

        companies = Company.objects.filter(
            Q(name__contains(query_dict['search'])) |
            Q(description__contains(query_dict['search']))
        )
        if (valid_dict['type']):
            companies = companies.filter(type=query_dict['type'])

        if (valid_dict['within'] & query_dict['within'] > 0):
            dist = query_dict['within']/COORDINATE_TO_MILES
            lat_max = query_dict['lat'] + dist
            lat_min = query_dict['lat'] - dist
            lon_max = query_dict['lon'] + dist
            lon_min = query_dict['lon'] - dist
            companies = companies.filter(
                (Q(coordinatesLat__lte=lat_max) |
                Q(coordinatesLat__gte=lat_min)) &
                (Q(coordinatesLat__lte=lon_max) |
                Q(coordinateLat__gte=lon_min))
            )

        print(companies)

        return ''
    else:
        raise Http404()
