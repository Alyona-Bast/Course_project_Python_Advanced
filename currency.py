from requests import get
import json

def currency():
    try:
        res = get("https://api.monobank.ua/bank/currency")
        usd_sell = json.loads(res.text)[0]['rateSell']
        usd_buy = json.loads(res.text)[0]['rateBuy']
        eur_sell = json.loads(res.text)[1]['rateSell']
        eur_buy = json.loads(res.text)[1]['rateBuy']
        return f'\tUSD \U0001f1fa\U0001f1f8 :\n' \
               f'Купівля: {usd_buy}\n' \
               f'Продаж: {usd_sell}\n' \
               f'\tEUR \U0001f1ea\U0001f1fa :\n' \
               f'Купівля: {eur_buy}\n' \
               f'Продаж: {eur_sell}\n'
    except:
        return f'Cпробуйте пізніше. "Монобанк" задумався \U0001F914'


