import requests
from config import API_KEY, BASE_URL

def get_current_weather(city):
    url = f"{BASE_URL}/current.json"
    params = {"key": API_KEY, "q": city}
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_forecast(city, days=3):
    url = f"{BASE_URL}/forecast.json"
    params = {"key": API_KEY, "q": city, "days": days}
    response = requests.get(url, params=params)
    data = response.json()
    return data
