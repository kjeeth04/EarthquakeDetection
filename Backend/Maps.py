# take in 
""""
Return magnatude   alert level , depth 

"""

# grab users location and use it to find where they should go
"""
given episenter location and user location. generate a path bewtween anywhere away from the episener

"""
import requests
def UserGeoData(user_IP):
    url = "https://ipgeolocation.abstractapi.com/v1"
    querystring = {"api_key":"fc515b2057234d9e8f35a6dbaa91dfcc",
                   "ip_address": f"{user_IP}" } # 166.171.248.255
    response = requests.request("GET", url, params=querystring)
    return response.json()["latitude"], response.json()["longitude"] # returns lat and long of user

def geolocationRadius(location,mag):
    base = 10
    match mag:
        case 5:
            radius = base * 1
        case 6:
            radius = base * 10
        case 7:
            radius = base * 100
        case 8:
            radius = base * 1000
        case 9:
            radius = base * 10000
        case 10:
            radius = base * 100000
    
    return radius
import math
         # USER LOCATION LAT-LONG     EPICENTER LOCATION LAT LONG
def distance(UserLO,QuakLO): #lat1, lon1, lat2, lon2
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(UserLO[0])# lat1 lon 1 lat2 lon 2
    lon1 = math.radians(UserLO[1])
    lat2 = math.radians(QuakLO[0])
    lon2 = math.radians(QuakLO[1])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

print(round(distance(UserGeoData("166.171.248.255"),(39.927378, -75.177287))), "kilos")


