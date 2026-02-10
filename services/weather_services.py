import requests
from datetime import timedelta

WEATHER_API_URL = "http://api.weatherapi.com/v1/forecast.json"
BAD_WEATHER = {"rain", "storm", "snow", "thunder", "drizzle"}

def get_weather_forecast(city, api_key, days):
    params = {
        "key": api_key,
        "q": city,
        "days": days,
        "aqi": "no",
        "alerts": "no"
    }
    r = requests.get(WEATHER_API_URL, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def build_weather_rows(start_date, forecast, trip_days):
    rows = []
    for i in range(trip_days):
        date = start_date + timedelta(days=i)
        f = next(
            (d for d in forecast["forecast"]["forecastday"] if d["date"] == str(date.date())),
            None
        )
        if f:
            rows.append({
                "day": i + 1,
                "date": str(date.date()),
                "condition": f["day"]["condition"]["text"],
                "min": f["day"]["mintemp_c"],
                "max": f["day"]["maxtemp_c"],
            })
    return rows
