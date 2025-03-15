# ## Task 1: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the `requests` library to fetch weather data for a specific city
# (ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

import requests
import json 
API_KEY = "4fed8f7469ce68919c6950cffc3ff9d5" 
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"

def get_weather(lat, lon):
    """Fetch and display weather data using latitude & longitude."""
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(WEATHER_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city = data.get("name", "Unknown")
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        print(f"\n City: {city}\n Temperature: {temp}°C\n Weather: {weather_desc}\n")
    else:
        print(f" Error: {response.status_code}, {response.json()}")

def get_lat_lon(city_name):
    """Fetch latitude & longitude of a city using OpenWeather's Geocoding API."""
    params = {
        "q": city_name,
        "limit": 1,
        "appid": API_KEY
    }
    response = requests.get(GEO_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["lat"], data[0]["lon"]
        else:
            print(" City not found!")
            return None, None
    else:
        print(f" Error: {response.status_code}, {response.json()}")
        return None, None

def main():
    """Menu-driven weather app."""
    while True:
        print("\n Welcome to Weather App")
        print("1️ Enter a city name")
        print("2️ Enter latitude & longitude manually")
        print("3️ Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            city = input("Enter city name: ").strip()
            lat, lon = get_lat_lon(city)
            if lat and lon:
                get_weather(lat, lon)
        
        elif choice == "2":
            try:
                lat = float(input("Enter latitude: "))
                lon = float(input("Enter longitude: "))
                get_weather(lat, lon)
            except ValueError:
                print(" Invalid input! Please enter numbers.")
        
        elif choice == "3":
            print(" Exiting...")
            break
        
        else:
            print(" Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


