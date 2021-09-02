from django.http import HttpResponse

from currency.utils import generate_password as gen_pass

from currency.models import Rate, ContactUs

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rate_list': rates,
    }

    return render(request, 'rate_list.html', context=context)


def contact_us(request):
    contacts = ContactUs.objects.all()
    context = {
        'contact_us': contacts,
    }

    return render(request, 'contact_us.html', context=context)


def response_codes(request):
    response = HttpResponse('Response', status=301, headers={'Location': 'https://google.com'})
    return response

def tables(request):
    return render(request, 'tmp.html')