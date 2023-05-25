import requests


class CityWeather:
    """
    Class for downloading weather data by city name
    """

    def __init__(self, api_key, city_name):
        self.__key = api_key
        self.city = city_name
        self.__show_current_weather()

    def __show_current_weather(self):

        if self.__get_city_coordinates() and self.__get_current_weather():
            self.__get_weather_parameters()
            print(f'\nCity: {self.city.title()} ({self.country}, {self.state})\n'
              f'Temperature: {self.temperature} Celsius\n'
              f'Atmospheric pressure: {self.pressure} hPa\n'
              f'Humidity: {self.humidity} in percentage\n'
              f'Description: {self.description}.\n')
        else:
            print("\n...City Not Found...\n")

    def __get_city_coordinates(self):

        url_coordinates = f"https://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=1&appid={self.__key}"
        response_coordinates = requests.get(url_coordinates)
        if coordinates_dict := response_coordinates.json():
            self.lat = coordinates_dict[0]['lat']
            self.lon = coordinates_dict[0]['lon']
            self.country = coordinates_dict[0]['country']
            try:
                self.state = coordinates_dict[0]['state']
            except KeyError:
                self.state = None
            return True
        return False

    def __get_current_weather(self):

        url_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.__key}&units=metric'
        response_weather = requests.get(url_weather)
        self.weather_dict = response_weather.json()
        return self.weather_dict["cod"] != "404"

    def __get_weather_parameters(self):
        main_key = self.weather_dict["main"]
        self.temperature = main_key["temp"]
        self.pressure = main_key["pressure"]
        self.humidity = main_key["humidity"]
        weather_key = self.weather_dict["weather"]
        self.description = weather_key[0]["description"]


if __name__ == "__main__":
    key_api = "293457267ffc0bcb3c59ab9aa6726d53"
    while True:
        if name_city := input("Enter city name : "):
            weather_checker = CityWeather(key_api, name_city)
        else:
            print('\n...END...\n')
            break
