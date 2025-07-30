# 🧳 Travel Budget Estimator

This is a Python-based smart travel assistant project under the domain of **Artificial Intelligence**. It estimates the total travel budget for a trip based on various user inputs such as travel mode, number of members, stay duration, activities, and fuel cost. The system uses geolocation services and real-time data scraping for accurate distance and pricing.

---

## 📦 Features

- Calculates geodesic distance between source and destination
- Estimates travel, fuel, food, activity, and stay costs
- Supports dynamic fuel price fetching from the internet
- Formats output in Indian currency
- Simple and modular code structure

---

## 📁 Project Structure

```
travel-budget-estimator/
│
├── main.py                  # Entry point
├── userinput.py             # Handles user inputs
├── location.py              # Geocoding and distance calculation
├── traveldata.py            # Fetch travel, fuel, and activity costs
├── budget.py                # Calculates the final budget breakdown
├── currency.py              # Formats currency to Indian format
├── fuelprice.py             # Constants: default mileage & fuel prices
└── README.md                # Project documentation
```

---

## ⚙️ Requirements

- geopy  
- requests  
- beautifulsoup4  

Install all with:

```bash
pip install geopy requests beautifulsoup4
```

---

## 🚀 How to Run

```bash
python main.py
```

Then, follow the interactive prompts to enter trip details.

---

## 📌 Notes

- Enter `0` if there are no activities planned.
- Fuel cost is automatically skipped if the travel mode is not car or bike.
- Invalid or unrecognized places will result in a warning.

---

## 🧠 Domain

**Artificial Intelligence** — by automating real-world planning through data-driven logic and external data sources.

---

## 🧑‍💻 Created By

Aswin – Second-year AIML Student
