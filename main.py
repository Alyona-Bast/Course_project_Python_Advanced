from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from transliterate import translit

import const
import menu_key
from weather import weather, sun
from currency import currency
from date import date


#Ініціалізація бота
bot = Bot(token=const.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


#Створення станів для введення назви міста
class StateGroupCity(StatesGroup):
    city_for_weather = State()
    city_for_sun = State()


#Повідомлення при натисканні старту
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Привіт, {0.first_name}!\n"
                           "Я бот з курсової Лимар Альони. "
                           "Яка інформація тебе цікавить?".format(message.from_user),
                           reply_markup=menu_key.menu)


#Головне меню
@dp.message_handler()
async def bot_menu(message: types.Message):
    if message.text == 'Погода':
        await bot.send_message(message.from_user.id, "Яке місто цікавить?")
        await StateGroupCity.city_for_weather.set()
    elif message.text == 'Схід/захід Сонця':
        await bot.send_message(message.from_user.id, "Яке місто цікавить?")
        await StateGroupCity.city_for_sun.set()
    elif message.text == 'Курс валют':
        await bot.send_message(message.from_user.id, currency())
    elif message.text == 'Про дату':
        await bot.send_message(message.from_user.id, date())
    else:
        await bot.send_message(message.from_user.id, "Не зрозумів команду")


#Хендлер стану для погоди
@dp.message_handler(state=StateGroupCity.city_for_weather)
async def weather_city(message: types.Message, state: FSMContext):
    city = translit(message.text, language_code="uk", reversed=True)
    await bot.send_message(message.from_user.id, weather(city))
    await state.finish()


#Хендлер стану для сонця
@dp.message_handler(state=StateGroupCity.city_for_sun)
async def weather_city(message: types.Message, state: FSMContext):
    city = translit(message.text, language_code="uk", reversed=True)
    await bot.send_message(message.from_user.id, sun(city))
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
