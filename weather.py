from urllib import response
from platform import python_version
import requests
import json

print("--------------------------------------")
print("Current Python Version-", python_version())
print("--------------------------------------")


API_KEY = "81bc5b7c36d8cca6868ca53d89d65122"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter the city: ")
request_url = f"{BASE_URL}?&appid={API_KEY}&q={city}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    print(data)
    with open("weather.json", "w") as write_file:
        json.dump(data, write_file)
else:
    print("Oops!")