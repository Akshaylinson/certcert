











import requests

def get_weather(city_name, api_key):
    # Set units to 'metric' for Celsius or 'imperial' for Fahrenheit
    url = f"http://openweathermap.org{city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {desc.capitalize()}")
    else:
        print("Error: Could not find city or API key is invalid.")

# Replace with your actual API key from OpenWeatherMap
MY_API_KEY = "your_api_key_here"
city = input("Enter city name: ")
get_weather(city, MY_API_KEY)























import requests

def get_weather(city_name, api_key):
    # Set units to 'metric' for Celsius or 'imperial' for Fahrenheit
    url = f"http://openweathermap.org{city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {desc.capitalize()}")
    else:
        print("Error: Could not find city or API key is invalid.")

# Replace with your actual API key from OpenWeatherMap
MY_API_KEY = "your_api_key_here"
city = input("Enter city name: ")
get_weather(city, MY_API_KEY)

