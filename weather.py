from requests import get
import datetime
from transliterate import translit

import const


def weather(city):
    try:
        weather_api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={const.key}&units=metric'
        response = get(weather_api)
        weather_dic = response.json()
        weather = weather_dic["weather"][0]["main"]
        city_uk = translit(city, language_code="uk").capitalize()
        if weather in const.code_to_smile:
            wd = const.code_to_smile[weather]
        else:
            wd = "Щоб дізнатися погоду, вигляни у вікно!"
        temperature = weather_dic["main"]["temp"]
        feels_like = weather_dic["main"]["feels_like"]
        pressure = weather_dic["main"]["pressure"]
        wind = weather_dic["wind"]["speed"]
        return f'В місті {city_uk} {wd}\n' \
               f'Температура повітря: {temperature} °C\n' \
               f'Відчувається як: {feels_like} °C\n' \
               f'Атмосферний тиск: {pressure} мм.рт.ст\n' \
               f'Вітер: {wind} м/с\n'
    except KeyError:
        return f"Перевірте назву міста!"


def sun(city):
    try:
        weather_api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={const.key}&units=metric'
        response = get(weather_api)
        weather_dic = response.json()
        sunrise_y = datetime.datetime.fromtimestamp(weather_dic["sys"]["sunrise"])
        sunrise = datetime.datetime.fromtimestamp(weather_dic["sys"]["sunrise"]).strftime('%H:%M')
        sunset_y = datetime.datetime.fromtimestamp(weather_dic["sys"]["sunset"])
        sunset = datetime.datetime.fromtimestamp(weather_dic["sys"]["sunset"]).strftime('%H:%M')
        length_day = sunset_y - sunrise_y
        city_uk = translit(city, language_code="uk").capitalize()
        return f'В місті {city_uk} \n' \
               f'сонце сходить о {sunrise}\n' \
               f'заходить о {sunset}\n' \
               f'Тривалість дня: {length_day}\n'
    except KeyError:
        return f"Перевірте назву міста!"


