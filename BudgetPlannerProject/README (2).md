# 🧠 AI Budget Planner

A Python-based smart assistant that estimates travel budgets using real-world data like geolocation, fuel prices, and user preferences. Developed under the domain of **Artificial Intelligence**, it helps plan budgets for business or family trips with reliable cost estimation.

## 📦 Features

* Geodesic distance calculation between locations
* Travel, fuel, food, activity, and stay cost estimation
* Real-time fuel price fetching (Petrol/Diesel supported)
* Budget breakdown formatted in Indian Rupees (₹)
* Clean, modular code structure


## 📁 Project Structure

```
ai-budget-planner/
│
├── main.py                  # Entry point
├── userinput.py             # Handles user inputs
├── location.py              # Coordinates & distance
├── traveldata.py            # Travel, fuel, and activity costs
├── budget.py                # Final budget calculation
├── currency.py              # Indian currency formatter
├── fuelprice.py             # Default rates & mileage
└── README.md                # Project documentation
```

---

## ⚙️ Requirements

* `geopy`
* `requests`
* `beautifulsoup4`

Install all dependencies:

```bash
pip install geopy requests beautifulsoup4
```

---

## 🚀 How to Run

```bash
python main.py
```

Follow the terminal prompts to enter your trip details.

---

## 📌 Notes

* Use `0` if no activities are planned.
* Fuel cost applies only to car or bike travel modes.
* If a location is invalid, default handling is applied.

---

## 🧠 Domain

**Artificial Intelligence** – Budget planning powered by data, logic, and real-time integration.

---

## 👤 Created By

**Aswin** – Second-year AIML Student

