from requests import get
from googletrans import Translator
from datetime import date


date_today = date.today().strftime("%m/%d")
translator = Translator()


def date():
    res = get(f"http://numbersapi.com/{date_today}/date")
    en_text = res.text
    trans = translator.translate(en_text, dest="uk").text
    return trans



