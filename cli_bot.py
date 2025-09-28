from weather_api import get_current_weather, get_forecast
from formatter import format_current_weather, format_forecast

def run_bot():
    print("Weather Bot (powered by WeatherAPI.com)")
    print("Type 'quit' to exit.\n")

    while True:
        city = input("Enter city: ")
        if city.lower() == "quit":
            break

        choice = input("Do you want (1) Current weather or (2) Forecast? ")

        if choice == "1":
            data = get_current_weather(city)
            print(format_current_weather(data))
        elif choice == "2":
            data = get_forecast(city, days=3)
            print(format_forecast(data))
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_bot()
