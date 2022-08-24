'''Example on how to use f-string '''

API_KEY = ""

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = "Vienna"

with open("key.txt","r") as f:
    API_KEY = f.read()

request_url = f"{BASE_URL}?&appid={API_KEY}&q={city}"

print(request_url)