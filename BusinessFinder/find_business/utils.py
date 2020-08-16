import math

COORDINATE_TO_MILES = 75.0

class utils(object):

    @staticmethod
    def findDistance(lat1, lon1, lat2, lon2):
        lat_diff = lat2 - lat1
        lon_diff = lon2 - lon1

        miles_x = lat_diff * COORDINATE_TO_MILES
        miles_y = lon_diff * COORDINATE_TO_MILES

        dist = miles_x**2 + miles_y**2
        return math.sqrt(dist)