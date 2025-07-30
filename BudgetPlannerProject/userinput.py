def get_user_inputs():
    print("Welcome to Budget Planner.. Please Enter your following details..")
    members = int(input("Number of members: "))
    current = input("Current location: ") 
    destination = input("Destination(City if possible): ") 
    stay_duration = int(input("Duration of stay (days): ")) 
    mode_of_travel = input("Mode of travel: ").lower()
    
    fuel_type = None
    if mode_of_travel in ['car', 'bike']:
        fuel_type = input("Fuel type (petrol/diesel): ").lower()

    travel_date = input("Date of travel (YYYY-MM-DD): ")
    print(" Next is your activites.. If there are no activites enter 0. Else seperate the activites using comma")
    activities = input("Activities: ").split(',')

    return {
        'members': members,
        'current_location': current,
        'destination': destination,
        'stay_duration': stay_duration,
        'mode_of_travel': mode_of_travel,
        'fuel_type': fuel_type,
        'travel_date': travel_date,
        'activities': [act.strip() for act in activities]
    }
