import requests
from flask import Flask, render_template, request, url_for 
import os
from urllib.parse import quote
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_url_path="/static") #initialising the app

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/weather", methods=['POST'])
def get_weather():
    city = request.form['city']
    city_name = quote(city)

    api_key = os.getenv('api_key')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)
    weather_data = response.json()
    # print (weather_data)

    if response.status_code == 200:
        data = {
           "city": weather_data['name'],
            "temp": weather_data['main']['temp'],
            "description": weather_data['weather'][0]['description'],
            "icon": weather_data['weather'][0]['icon']
        }
        return render_template('weather.html', data=data)
    
    else:
        return render_template("error.html",  err_ymessage="Page could not be found")

if __name__ == "__main__":
    app.run(debug=True)