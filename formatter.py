def format_current_weather(data):
    if "error" in data:
        return f"Error: {data['error']['message']}"

    loc = data["location"]
    cur = data["current"]
    icon_url = "http:" + cur["condition"]["icon"]

    # Return a dict for easy HTML rendering
    return {
        "location": f"{loc['name']}, {loc['country']}",
        "temp": f"{cur['temp_c']}°C",
        "condition": cur["condition"]["text"],
        "wind": f"{cur['wind_kph']} kph",
        "humidity": f"{cur['humidity']}%",
        "icon": icon_url
    }

def format_forecast(data):
    if "error" in data:
        return f"Error: {data['error']['message']}"

    loc = data["location"]
    forecast_days = data["forecast"]["forecastday"]

    # Return list of dicts for HTML rendering
    forecasts = []
    for day in forecast_days:
        forecasts.append({
            "date": day["date"],
            "avg_temp": f"{day['day']['avgtemp_c']}°C",
            "condition": day["day"]["condition"]["text"],
            "icon": "http:" + day["day"]["condition"]["icon"]
        })
    return {"location": f"{loc['name']}, {loc['country']}", "forecasts": forecasts}
