from django import template
import math

register = template.Library()

COORDINATE_TO_MILES = 75.0

@register.simple_tag
def findDistance(lat1, lon1, lat2, lon2):
    lat_diff = lat2 - float(lat1)
    lon_diff = lon2 - float(lon1)

    miles_x = lat_diff * COORDINATE_TO_MILES
    miles_y = lon_diff * COORDINATE_TO_MILES

    dist = miles_x**2 + miles_y**2
    return round(math.sqrt(dist), 2)