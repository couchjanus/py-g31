import requests

import json

URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

def load_exchange():
    return json.loads(requests.get(URL).text)

# print(load_exchange())

def get_exchange(ccy_key):
    for e in load_exchange():
        if ccy_key == e['ccy']:
            return e
    return False
