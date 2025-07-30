def predict_budget(members, distance, travel_cost, fuel_cost, activity_cost, stay_days):
    total_travel = travel_cost * members
    total_fuel   = fuel_cost
    total_act    = activity_cost * members
    stay_per_day = 1000.0
    total_stay   = stay_per_day * members * stay_days
    food_per_day = 500.0
    total_food   = food_per_day * members * stay_days

    total = total_travel + total_fuel + total_act + total_stay + total_food
    return {
        'travel': total_travel,
        'fuel': total_fuel,
        'activities': total_act,
        'stay': total_stay,
        'food': total_food,
        'total': total
    }