AI Travel Budget Estimator 
----------------

Project Summary:
This project is a terminal-based Python application that helps users estimate their travel expenses intelligently based on various real-world parameters. It is designed under the domain of Artificial Intelligence and integrates geolocation data, fuel prices, and user input to generate a complete travel budget.
 
Project Idea:
The core idea of this project is to assist in planning budgets for business or family trips. It provides an approximate estimate of the total trip cost based on user inputs. By leveraging advanced AI techniques, it determines location coordinates, fetches real-time prices for fuel, accommodations, and transportation (such as trains and flights), and delivers a highly accurate budget forecast for the journey.

Key Features:
1. Distance-Based Travel Estimation
The system takes the current location and destination from the user, converts them into geographic coordinates using the geopy library, and calculates the real-world distance (in kilometers) between them using geodesic methods.
2. Fuel Cost Calculation
For personal transport modes like car or bike, the system calculates fuel cost using:
    • Distance
    • Default mileage
    • Real-time fuel price scraped from the internet (GoodReturns website)
If the fuel price cannot be fetched, a default rate is used.
3. Travel Cost for Public Transport
If the user selects a mode other than car or bike, a placeholder travel cost is applied (can be expanded to real ticket cost integration later).
4. Activity Cost Estimation
Users can enter optional activities for the trip. Each valid activity adds a fixed cost to the total budget. If the user enters 0, no activity cost is added.
5. Stay and Food Expenses
Stay cost is calculated at ₹1000 per member per day.
Food cost is calculated at ₹500 per member per day.
These rates can be customized in the budget module.
6. Indian Currency Formatting
All estimated costs are displayed in neatly formatted Indian Rupees (₹), with thousands separators and two decimal precision.

Domain: Artificial Intelligence , Machine Learning
Future Scope
    • Integration with APIs for live ticket prices and hotel bookings
    • Exporting reports to Excel or PDF
    • Web or mobile interface using Flask or React
    • Smart recommendations based on budget limits or trip type
