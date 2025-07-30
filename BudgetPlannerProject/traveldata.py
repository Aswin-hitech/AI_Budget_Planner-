import requests
from bs4 import BeautifulSoup
from fuelprice import DEFAULT_MILEAGE, FUEL_PRICES

def fetch_travel_cost(mode, source, destination, date):
    return 1000.0  

def fetch_fuel_price(location, fuel_type, distance_km):
    try:
        city = location.lower().replace(" ", "-")
        url = f"https://www.goodreturns.in/{fuel_type}-price-in-{city}.html"
        html = requests.get(url).text
        detail = BeautifulSoup(html, "html.parser")
        price = detail.find("td", text="Price").find_next("td").text
        rate_per_liter = float(price.replace("₹", "").strip())
    except:
        rate_per_liter = FUEL_PRICES["default"]

    total_liters = distance_km / DEFAULT_MILEAGE
    return rate_per_liter * total_liters

def fetch_activity_cost(activities, location):
    cleaned_activities = []
    if len(activities) == 1 and activities[0].strip() == '0':
        return 0
    for activity in activities:
        cleaned = activity.strip()
        if cleaned and cleaned != '0':
            cleaned_activities.append(cleaned)

    return len(cleaned_activities) * 500
