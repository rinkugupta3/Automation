# https://openweathermap.org/current#cityid
# https://home.openweathermap.org/api_keys

import requests
import json


api_key = 'dd7fd3601dc9f1d6b65223780f78662e'
city= 'Edison'

url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=imperial"

request = requests.get(url)
json_data = request.json()

print(json_data)

filename = 'weather.json'

try:
    with open(filename, 'w') as file:
        json.dump(json_data, file)
except IOError:
    print("Could not find files")

temp_min = json_data.get("main").get("temp_min")
print("Today temp is ",temp_min)
description = json_data.get("weather") [0].get("description")
print(description)