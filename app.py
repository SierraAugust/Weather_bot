from flask import Flask, render_template, request
from weather_api import get_current_weather, get_forecast
from formatter import format_current_weather, format_forecast

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    current = None
    forecast = None
    if request.method == "POST":
        city = request.form.get("city")
        choice = request.form.get("choice")

        if city:
            if choice == "current":
                data = get_current_weather(city)
                current = format_current_weather(data)
            else:
                data = get_forecast(city, days=3)
                forecast = format_forecast(data)

    return render_template("index.html", current=current, forecast=forecast)

if __name__ == "__main__":
    app.run(debug=True)
