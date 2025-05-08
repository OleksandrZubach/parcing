import requests
from requests.exceptions import HTTPError
from my_token import API_TOKEN

class Weather:
    def __init__(self):
        self.url='http://api.openweathermap.org/geo/1.0/direct'
        self.params={'q':'Lviv', 'limit':5,'appid':API_TOKEN}

    def get_cord(self):
        try:
            response=requests.get(self.url,params=self.params)
            response.raise_for_status()
            # print(response.json())
            lat=response.json()[0]['lat']
            lon=response.json()[0]['lon']
            return lat, lon
        except (HTTPError, ValueError) as er:
            print(f'Error is {er}')

    def get_weather(self,lat, lon):
        try:
            url_weather='https://api.openweathermap.org/data/2.5/weather'
            url_weather_params = {'lat':lat,'lon':lon,'appid':API_TOKEN , 'units':'metric','lang':'ua'}
            response_weather = requests.get(url_weather,params=url_weather_params)
            response_weather.raise_for_status()
            print(response_weather.json())
            print(response_weather.json()['weather'][0]['description'])
            print(response_weather.json()['main']['temp_min'])
        except (HTTPError, ValueError) as er:
            print(f'Error is {er}')

if __name__ == '__main__':
    weather=Weather()
    lat, lon=weather.get_cord()
    print(lat, lon)
    weather.get_weather(lat,lon)
