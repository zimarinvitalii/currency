import requests


currency_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

response = requests.get(currency_url)

rates = response.json()


for rate in rates:
    if rate['cc'] in ('USD', 'EUR'):
        currency_type = rate['cc']
        sale = rate['rate']
        print(currency_type, sale)




