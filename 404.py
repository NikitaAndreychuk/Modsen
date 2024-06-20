import requests


api_key = "2e5281540cb03fa89dda71fdd35a7a6d"
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Minsc",
    "appid": api_key
}


response = requests.get(url, params=params)
print(response.status_code, response.text)