AI BUDGET PLANNER

## 🧾 **Project Summary**

This project is a terminal-based Python application that intelligently estimates travel expenses based on real-world parameters. Designed under the domain of Artificial Intelligence, it integrates geolocation, live fuel pricing, transport modes, and user-defined preferences to generate a smart travel budget.

## 💡 **Project Idea**

The core idea is to help users (individuals or families) plan their trip budgets more accurately. By combining AI concepts with real-time data like location coordinates and fuel prices, the system provides an approximate and reliable cost forecast for trips across different transport modes.

🚀 **Key Features**

* **Live Fuel Price Support (Petrol/Diesel)**
  Fetches real-time fuel prices using web scraping based on user-selected fuel type and destination city.

* **Accurate Distance Calculation**
  Converts source and destination into coordinates using geopy and computes distance using geodesic method.

* **Vehicle-based Travel Cost**
  For cars and bikes, calculates fuel cost using mileage, distance, and live fuel rates. For buses, uses a flat fare formula (distance/2).

* **Activity Cost Estimation**
  Adds ₹500 per valid activity entered. Supports skipping activities with a simple input.

* **Stay & Food Expense Estimation**
  Stay: ₹1000 per member/day
  Food: ₹500 per member/day
  *(Customizable in the budget module)*

* **Formatted Output**
  All expenses are displayed in Indian Rupees (₹) with proper formatting.

## 🧠 **Domain**
Artificial Intelligence, Machine Learning

## 🔭 **Future Scope**
* API Integration for live hotel, train, and flight rates
* Export final report to PDF or Excel
* Web/mobile version with Flask or React
* Smart suggestions based on trip type or budget range
