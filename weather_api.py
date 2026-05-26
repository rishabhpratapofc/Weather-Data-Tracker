import requests
import pandas as pd
import os

from datetime import datetime


api_key = "fce058a9cc6abdbec6eca7da55c85d2b"


city = input("Enter city name: ")


url = "https://api.openweathermap.org/data/2.5/weather"


params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}


response = requests.get(url, params=params)

data = response.json()

if data.get("cod") != 200:
    print("Invalid city name")
    print("API Message:", data.get("message"))
    exit()


#  extract data from response

city_name = data["name"]

country_name = data["sys"]["country"]

temperature = data["main"]["temp"]

humidity = data["main"]["humidity"]

wind_speed = data["wind"]["speed"]

pressure = data["main"]["pressure"]

weather_condition = data["weather"][0]["description"]

cloud_percentage = data["clouds"]["all"]


current_time = datetime.now()

current_date = current_time.strftime("%Y-%m-%d")

current_clock = current_time.strftime("%H:%M:%S")

day_name = current_time.strftime("%A")

hour = current_time.hour



# WEATHER ANALYSIS

if temperature >= 40:
    temp_status = "Very Hot Weather"

elif temperature >= 30:
    temp_status = "Moderate Weather"

else:
    temp_status = "Cool Weather"


if humidity >= 80:
    humidity_status = "High Humidity"

elif humidity >= 50:
    humidity_status = "Moderate Humidity"

else:
    humidity_status = "Low Humidity"


if wind_speed >= 10:
    wind_status = "Strong Wind"

else:
    wind_status = "Normal Wind"


if cloud_percentage >= 70:
    cloud_status = "Cloudy Sky"

elif cloud_percentage >= 30:
    cloud_status = "Partially Cloudy"

else:
    cloud_status = "Clear Sky"



# WEATHER REPORT

print("\n--- Weather Report ---")

print("Time:", current_clock)

print("Date:", current_date)

print("Day:", day_name)

print("City:", city_name)

print("Country:", country_name)

print("Temperature:", temperature, "°C")

print("Humidity:", humidity, "%")

print("Wind Speed:", wind_speed)

print("Pressure:", pressure)

print("Weather:", weather_condition)

print("Clouds:", cloud_percentage, "%")



# WEATHER ANALYSIS REPORT

print("\n--- Weather Analysis ---")

print(temp_status)

print(humidity_status)

print(wind_status)

print(cloud_status)



# CREATE DATASET

weather_data = {

    "Date": current_date,

    "Time": current_clock,

    "Day": day_name,

    "Hour": hour,

    "City": city_name,

    "Country": country_name,

    "Temperature": temperature,

    "Humidity": humidity,

    "Wind_Speed": wind_speed,

    "Pressure": pressure,

    "Weather": weather_condition,

    "Clouds": cloud_percentage,

    "Temp_Status": temp_status,

    "Humidity_Status": humidity_status,

    "Wind_Status": wind_status,

    "Cloud_Status": cloud_status
}



# CREATE DATAFRAME

df = pd.DataFrame([weather_data])



# CHECK FILE EXISTENCE


file_exists = os.path.isfile("weather_data.csv")



# SAVE CSV IN APPEND MODE


df.to_csv(
    "weather_data.csv",
    mode="a",
    header=not file_exists,
    index=False
)

print("\nData saved successfully in weather_data.csv")