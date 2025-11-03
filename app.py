from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form["city"]
        try:
            response = requests.get(BASE_URL, params = {"q": city, "appid": API_KEY, "units": "metric"})
            response.raise_for_status()
            data = response.json()

            weather_data = {
                "city": city.title(),
                "temperature": round(data["main"]["temp"], 1),
                "description": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"]
            }

        except requests.exceptions.RequestException:
            return render_template("error.html", message = "Unable to fetch weather data. Check your network or API key.")
        except KeyError:
            return render_template("error.html", message = "Invalid city name. Please try again.")
        
    return render_template('index.html', weather=weather_data, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)