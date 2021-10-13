import requests
from currency.models import Rate
from decimal import Decimal
from bs4 import BeautifulSoup


def round_currency(num):
    return Decimal(num).quantize(Decimal('.01'))


currency_url = 'https://api.monobank.ua/bank/currency'

response = requests.get(currency_url)

response.raise_for_status()  # raise error if status_code is not 2xx

source = 'monobank'



available_currency_types = (840, 978)

rates = response.json()

for rate in rates:
    currency_type = rate['currencyCodeA']
    if currency_type in available_currency_types:
        sale = round_currency(rate['rateSell'])
        buy = round_currency(rate['rateBuy'])

        last_rate = Rate.objects.filter(
            type=currency_type,
            source=source,
        ).order_by('created').last()



    if (
            last_rate is None or
            last_rate.sale != sale or
            last_rate.buy != buy
    ):
        Rate.objects.create(
            type=currency_type,
            sale=sale,
            buy=buy,
            source=source,
        )
