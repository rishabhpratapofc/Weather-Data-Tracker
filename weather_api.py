import requests
import pandas as pd
import os
from datetime import datetime

api_key = "fce058a9cc6abdbec6eca7da55c85d2b"

cities = [
"Amaravati",
"Itanagar",
"Dispur",
"Patna",
"Raipur",
"Panaji",
"Gandhinagar",
"Chandigarh",
"Shimla",
"Ranchi",
"Bengaluru",
"Thiruvananthapuram",
"Bhopal",
"Mumbai",
"Imphal",
"Shillong",
"Aizawl",
"Kohima",
"Bhubaneswar",
"Jaipur",
"Gangtok",
"Chennai",
"Hyderabad",
"Agartala",
"Lucknow",
"Dehradun",
"Kolkata",
"Mainpuri",
"Ludhiana",
"Hisar",
"Nagpur",
"Nashik",
"Kanpur",
"Pune",
"Coimbatore"
]

url = "https://api.openweathermap.org/data/2.5/weather"

all_weather_data = []

for city in cities:
    try:
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        city_name = data["name"]

        temprature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]

        weather_condition = data["weather"][0]["description"]
        cloudiness = data["clouds"]["all"]

        now = datetime.now()

        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        day_name = now.strftime("%A")
        hour = now.hour

        if temprature >= 40:
            temp_status = "Very Hot Weather"
        elif temprature >= 30:
            temp_status = "Moderate Weather"
        else:
            temp_status = "Cold Weather"

        if humidity >= 80:
            humidity_status = "High Humidity"
        elif humidity >= 50:
            humidity_status = "Moderate Humidity"
        else:
            humidity_status = "Low Humidity"

        if wind_speed >= 10:
            wind_status = "Strong Wind"
        elif wind_speed >= 5:
            wind_status = "Moderate Wind"
        else:
            wind_status = "Calm Wind"

        if cloudiness >= 80:
            cloud_status = "Cloudy"
        elif cloudiness >= 50:
            cloud_status = "Partly Cloudy"
        else:
            cloud_status = "Clear Sky"

        weather_data = {
            "Date": current_date,
            "Time": current_time,
            "Day": day_name,
            "Hour": hour,
            "City": city_name,
            "Temperature": temprature,
            "Humidity": humidity,
            "Wind_Speed": wind_speed,
            "Pressure": pressure,
            "Weather_Condition": weather_condition,
            "Cloudiness": cloudiness,
            "Temperature_Status": temp_status,
            "Humidity_Status": humidity_status,
            "Wind_Status": wind_status,
            "Cloudiness_Status": cloud_status
        }

        all_weather_data.append(weather_data)

        print(f"✓ {city_name} collected")

    except Exception as e:
        print(f"✗ Error collecting {city}")
        print(e)


df = pd.DataFrame(all_weather_data)

file_name = "weather_data_auto.csv"

file_exists = os.path.isfile(file_name)

df.to_csv(
file_name,
mode="a",
header=not file_exists,
index=False,
encoding="utf-8"
)

print("\n=================================")
print(f"Total Records Added : {len(df)}")
print("Data saved successfully")
print("=================================")
