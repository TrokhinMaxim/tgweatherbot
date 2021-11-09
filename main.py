import requests
import datetime as dt
from config import weather_token, bot_token
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pprint import pprint


def get_weather(city, weather_token):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric'
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        today = dt.date.today()

       print(f'Сегодня {today}\n'
              f'Погода в городе {city}\nТемпература {int(cur_weather)}°С\n'
              f'Влажность {humidity}%\nДавление {pressure} Па\nСкорость ветра {wind_speed} м/c'
              )
    except Exception as ex:
        print(ex)
        print('Проверьте название города')




def main():
    city = input('Введите город ')
    get_weather(city, weather_token)


if __name__ == '__main__':
    main()














