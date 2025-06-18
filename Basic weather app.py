Basic code for the Project:
#UPPANANTHALA GANESH
import requests

api_key = "d005de8952d81f8575b646533fba426a"
base_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    'q': city,
    'appid': api_key,
    'units': 'metric'
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    print(f"\nWeather in {city.capitalize()}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description.capitalize()}")
else:
    print("\nCity not found or API error. Please check the city name or your API key.") 
    
