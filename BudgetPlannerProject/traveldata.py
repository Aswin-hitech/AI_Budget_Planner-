import requests
from bs4 import BeautifulSoup
from fuelprice import Mileage, FUEL_PRICES  
from location import get_coordinates  # Should return (lat, lon) tuple
from geopy.distance import geodesic

def fetch_fuel_price(location, fuel_type, distance_km, vehicle_type):
    try:
        city = location.lower().replace(" ", "-")
        url = f"https://www.goodreturns.in/{fuel_type}-price-in-{city}.html"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        price_cell = soup.find("td", text="Price")
        if not price_cell:
            raise ValueError("Could not find price cell")

        price_text = price_cell.find_next("td").text
        rate_per_liter = float(price_text.replace("₹", "").strip())
    except Exception as e:
        print(f"[Warning] Could not fetch fuel price for {city}: {e}")
        rate_per_liter = FUEL_PRICES.get("default", 100.0)

    mileage = Mileage.get(vehicle_type, 20.0)
    if mileage == 0:
        print(f"[Error] Mileage for {vehicle_type} is zero. Avoiding division by zero.")
        return 0.0

    total_liters = distance_km / mileage
    return rate_per_liter * total_liters

def fetch_travel_cost(mode, source, destination, date, fuel_type='petrol'):
    coords1 = get_coordinates(source)
    coords2 = get_coordinates(destination)

    if not coords1 or not coords2:
        print("[Error] Could not calculate coordinates.")
        return 0.0

    distance = geodesic(coords1, coords2).km

    if mode in ['car', 'bike']:
        fuel_type = fuel_type.lower()
        if fuel_type not in ['petrol', 'diesel']:
            print(f"[Error] Unsupported fuel type: {fuel_type}. Defaulting to petrol.")
            fuel_type = 'petrol'

        return fetch_fuel_price(
            location=destination,
            fuel_type=fuel_type,
            distance_km=distance,
            vehicle_type=mode
        )
    elif mode == 'bus':
        return distance / 2
    else:
        return distance  # Fallback for other modes

def fetch_activity_cost(activities, location):
    if not activities or all(act.strip() == '0' for act in activities):
        return 0

    cleaned_activities = [
        act.strip() for act in activities
        if act.strip() and act.strip() != '0'
    ]
    return len(cleaned_activities) * 500
