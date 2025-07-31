def get_user_inputs():
    print("Welcome to Budget Planner.. Please Enter your following details..")

    while True:
        try:
            members = int(input("Number of members: "))
            if members <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid number greater than 0.")

    current = input("Current location: ").strip()
    destination = input("Destination (City if possible): ").strip()

    while True:
        try:
            stay_duration = int(input("Duration of stay (in days): "))
            if stay_duration <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid number of days.")

    mode_of_travel = input("Mode of travel (car/bike/train/flight/bus): ").strip().lower()

    fuel_type = None
    vehicle_type = None
    if mode_of_travel in ['car', 'bike']:
        fuel_type = input("Fuel type (petrol/diesel): ").strip().lower()
        vehicle_type = mode_of_travel 

    travel_date = input("Date of travel (YYYY-MM-DD): ").strip()

    print("\nNext is your activities. If none, enter 0. Else separate the activities using commas.")
    activities = input("Activities: ").split(',')

    return {
        'members': members,
        'current_location': current,
        'destination': destination,
        'stay_duration': stay_duration,
        'mode_of_travel': mode_of_travel,
        'fuel_type': fuel_type,
        'vehicle_type': vehicle_type,
        'travel_date': travel_date,
        'activities': [act.strip() for act in activities]
    }
