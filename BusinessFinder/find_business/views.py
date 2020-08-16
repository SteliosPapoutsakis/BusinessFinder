from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader

from django.db.models import Q

from .models import CompanyTypes, Company

#Constants that help with determining a default location
#and doing a very rough calculation from Latitude and
#longiture degrees to miles
COORDINATE_TO_MILES = 75.0
PORTLAND_LAT = 45.5732
PORTLAND_LON = -122.7276

# Send the default home page,
# before any location or search parameters
# are given
def index(request):
    companies = Company.objects.all()
    companies_dict = {
        'companies': companies,
        'lat': PORTLAND_LAT,
        'lon': PORTLAND_LON
    }
    return render(request, 'find_business/index.html', companies_dict)

# Queries for a list of businesses based on certain
# search parameters, these parameters include the
# company type, a search string and a within distance (mi)
# as well as the users current location
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

        if (valid_dict['search']):
            search = query_dict['search']
            companies = Company.objects.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(activities__icontains=search)
            )

        if (valid_dict['type']):
            mytype = CompanyTypes[query_dict['type']]
            companies = companies.filter(type=mytype)

        if (valid_dict['within'] & (query_dict['within'] != '0')):
            dist = float(query_dict['within'])/COORDINATE_TO_MILES
            print(dist)
            lat = float(query_dict['lat'])
            lon = float(query_dict['lon'])
            lat_max = lat + dist
            lat_min = lat - dist
            lon_max = lon + dist
            lon_min = lon - dist
            print(str(lat) + ' ' + str(lon))
            print(str(lat_max) + ' ' + str(lat_min) + ' ' + str(lon_max) + ' ' + str(lon_min))
            companies = companies.filter(
                (Q(coordinatesLat__lte=lat_max) &
                Q(coordinatesLat__gte=lat_min)) &
                (Q(coordinatesLon__lte=lon_max) &
                Q(coordinatesLon__gte=lon_min)))

        print(companies.all())

        companies_dict = {
            'companies': companies.all(),
            'lat': query_dict['lat'],
            'lon': query_dict['lon']
        }

        return render(request, 'find_business/businesses_list.html', companies_dict)

    else:
        raise Http404()

# Queries the database for all company names that are listed
# and returns a list of tuples decribing the location of each company
# that was requested
def locations_query(request):
    locations = []
    if request.method == 'POST':
        print(request.POST)
        names = request.POST.get('names[]')
        for companyName in names:
            companies = Company.objects.filter(name=companyName)
            if companies.count() != 0:
                comp = companies[0]
                locations.append((comp.locationLat, complocationLon))
            else:
                locations.append((45.0, -122.0))
    print(locations)
    return JsonResponse(locations, safe=False)
