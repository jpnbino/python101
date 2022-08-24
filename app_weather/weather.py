from urllib import response
from platform import python_version
import requests
import json

API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):  
    API_KEY = get_api_key()
    request_url = f"{BASE_URL}?&appid={API_KEY}&q={city}"
    
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        with open("weather.json", "w") as write_file:
            json.dump(data, write_file)
    else:
        print("Request error!")

def get_api_key():
    with open("key.txt","r") as f:
        return f.read()
        