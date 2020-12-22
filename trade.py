import requests
from config import *

BASE_URL = "https://paper-api.alpaca.markets/"

ACCOUNT_URL = "{}/V2/account".format(BASE_URL)

r = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY})

print(r.content)