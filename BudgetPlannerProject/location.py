from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time
geolocator = Nominatim(user_agent="travel_budget_app")

def get_coordinates(place_name):
    try:
        loc = geolocator.geocode(place_name)
        return (loc.latitude, loc.longitude) if loc else None
    except Exception as e:
        print(f"[Error geocoding] {e}")
        return None

def calculate_distance(coords1, coords2):
    if not coords1 or not coords2:
        return 0
    time.sleep(1) 
    return round(geodesic(coords1, coords2).kilometers, 2)