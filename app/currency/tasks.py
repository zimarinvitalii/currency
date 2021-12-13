from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import requests
from decimal import Decimal
from bs4 import BeautifulSoup
from currency.models import Rate
from currency import model_choices as mch


def round_currency(num):
    return Decimal(num).quantize(Decimal('.01'))


@shared_task
def debug_task(sleep_time: int = 5):
    from currency.models import Rate
    print(f'Count Rates: {Rate.objects.count()}')


@shared_task
def contact_us(subject, body):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():

    privatbank_currency_url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    response = requests.get(privatbank_currency_url)

    response.raise_for_status()  # raise error if status_code is not 2xx

    rates = response.json()
    source = 'privatbank'
    available_currency_types = {
        'USD': mch.TYPE_USD,
        'EUR': mch.TYPE_EUR,

    }
    for rate in rates:
        currency_type = rate['ccy']
        if currency_type in available_currency_types:
            sale = round_currency(rate['sale'])
            buy = round_currency(rate['buy'])
            ct = available_currency_types[currency_type]

            last_rate = Rate.objects.filter(
                type=ct,
                source=source,
            ).order_by('created').last()

        if (
                last_rate is None or
                last_rate.sale != sale or
                last_rate.buy != buy
        ):
            Rate.objects.create(
                type=ct,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parse_alfabank():
    alfabank_currency_url = 'https://old.alfabank.ua/'

    response = requests.get(alfabank_currency_url)

    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    usd_buy = soup.find("span", {"data-currency": "USD_BUY"}).text.strip()
    usd_sale = soup.find("span", {"data-currency": "USD_SALE"}).text.strip()

    rate_usd = {'ccy': 'USD', 'buy': usd_buy, 'sale': usd_sale}

    eur_buy = soup.find("span", {"data-currency": "EUR_BUY"}).text.strip()
    eur_sale = soup.find("span", {"data-currency": "EUR_SALE"}).text.strip()

    rate_eur = {'ccy': 'EUR', 'buy': eur_buy, 'sale': eur_sale}

    rates = (rate_eur, rate_usd)

    source = 'alfabank'
    available_currency_types = {
        'USD': mch.TYPE_USD,
        'EUR': mch.TYPE_EUR,

    }

    for rate in rates:
        currency_type = rate['ccy']
        if currency_type in available_currency_types:
            sale = round_currency(rate['sale'])
            buy = round_currency(rate['buy'])

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


@shared_task
def parse_govbank():
    govbank_currency_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

    response = requests.get(govbank_currency_url)

    response.raise_for_status()

    rates = response.json()

    source = 'govbank'
    available_currency_types = {
        'USD': mch.TYPE_USD,
        'EUR': mch.TYPE_EUR,

    }

    for rate in rates:
        currency_type = rate['cc']
        if currency_type in available_currency_types:

            sale = round_currency(rate['rate'])
            buy = 0

            last_rate = Rate.objects.filter(
                type=currency_type,
                source=source,
            ).order_by('created').last()

            if last_rate is None or last_rate.sale != sale:
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )



