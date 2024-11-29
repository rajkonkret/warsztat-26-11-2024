from typing import List

import requests
from pydantic import BaseModel

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)
print(response)  # <Response [200]>ok
# 3xx redirect, warningi
# 401,404, 400 bad request
# 500
print(response.text)
print(type(response.text))  # <class 'str'>

response_data = response.json()
print(response_data)


# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '232/A/NBP/2024', 'effectiveDate': '2024-11-29', 'mid': 4.077}]}

class Rates(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class Currency(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rates]


data = Currency(**response.json())
print(data)
# table = 'A'
# currency = 'dolar amerykański'
# code = 'USD'
# rates = [Rates(no='232/A/NBP/2024', effectiveDate='2024-11-29', mid=4.077)]

print(data.rates[0].mid) # 4.077

