from userinput import get_user_inputs
from location import get_coordinates, calculate_distance
from traveldata import fetch_fuel_price, fetch_travel_cost, fetch_activity_cost
from budget import predict_budget
from currency import indian_currency

def main():
    user_data = get_user_inputs()

    coords_src = get_coordinates(user_data['current_location'])
    coords_dst = get_coordinates(user_data['destination'])
    distance_km = calculate_distance(coords_src, coords_dst)

    travel_cost = fetch_travel_cost(
        user_data['mode_of_travel'],
        user_data['current_location'],
        user_data['destination'],
        user_data['travel_date'],
        user_data['fuel_type']  
    )
    fuel_cost = 0  # 
    activity_cost = fetch_activity_cost(user_data['activities'], user_data['destination'])

    budget = predict_budget(
        members=user_data['members'],
        distance=distance_km,
        travel_cost=travel_cost,
        fuel_cost=fuel_cost,  # Kept for compatibility
        activity_cost=activity_cost,
        stay_days=user_data['stay_duration']
    )

    print("\nEstimated Budget Breakdown:")
    for cat, amt in budget.items():
        print(f"  {cat.title():12}: {indian_currency(amt)}")

if __name__ == "__main__":
    main()
