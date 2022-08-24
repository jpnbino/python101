'''reads a field in a JSON file'''
import json

with open("weather.json","r") as read_file:
    data = json.load(read_file)


print(type(data))

#temperature in celcius
temperature = data['main']['temp_min'] - 273.15
print(temperature)