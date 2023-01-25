from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


#Головне меню
btnWeather = KeyboardButton('Погода')
btnSun = KeyboardButton('Схід/захід Сонця')
btnCurrency = KeyboardButton('Курс валют')
btnDate = KeyboardButton('Про дату')

menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnWeather, btnSun, btnCurrency, btnDate)






