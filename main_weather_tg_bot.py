from config import weather_token, bot_token
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime as dt


bot = Bot(token='1992222055:AAE0vFHoWGej_DHsshZwPrIqgEMd4-MMQVQ')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Пиши город - скажу погоду!')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:

        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric'
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        today = dt.date.today()

        await message.reply(f'Сегодня {today}\n'
              f'Погода в городе {city}\nТемпература {int(cur_weather)}°С\n'
              f'Влажность {humidity}%\nДавление {pressure} Па\nСкорость ветра {wind_speed} м/c'
              )


    except:
        await message.reply('Проверьте название города')


if __name__ == '__main__':
    executor.start_polling(dp)




