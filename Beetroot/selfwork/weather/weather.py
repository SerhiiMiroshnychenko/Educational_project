import requests

api_key = "293457267ffc0bcb3c59ab9aa6726d53"

city_name = input("Enter city name : ")

url_coordinates = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"

response_coordinates = requests.get(url_coordinates)

coordinates_dict = response_coordinates.json()

city_lat = coordinates_dict[0]['lat']
city_lon = coordinates_dict[0]['lon']
city_country = coordinates_dict[0]['country']
city_state = coordinates_dict[0]['state']

url_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid={api_key}&units=metric'

response_weather = requests.get(url_weather)

weather_dict = response_weather.json()

if weather_dict["cod"] != "404":

    main_key = weather_dict["main"]
    current_temperature = main_key["temp"]
    current_pressure = main_key["pressure"]
    current_humidity = main_key["humidity"]
    weather_key = weather_dict["weather"]
    weather_description = weather_key[0]["description"]

    print(f'\nCity: {city_name} ({city_country}, {city_state})\n'
          f'Temperature: {current_temperature} Celsius\n'
          f'Atmospheric pressure: {current_pressure} hPa\n'
          f'Humidity: {current_humidity} in percentage\n'
          f'Description: {weather_description}.')

else:
    print(" City Not Found ")
