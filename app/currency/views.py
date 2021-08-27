from django.http import HttpResponse

from currency.utils import generate_password as gen_pass

from currency.models import Rate, ContactUs

from django.shortcuts import render


def hello_world(request):
    return HttpResponse('Hello World')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)


def rate_list(request):
    rates = Rate.objects.all()

    result = []
    for rate in rates:
        # breakpoint
        rate.append(
            f'Id: {rate.id} Sale: {rate.sale} Buy: {rate.buy} </br>'
        )

    return HttpResponse(str(result))


def contact_us(request):
    contacts = ContactUs.objects.all()

    result = []
    for contact in contacts:
        # breakpoint
        contact.append(
            f'Id: {contact.id} Email: {contact.email_form} Subject: {contact.subject} Message: {contact.message}</br>'
        )

    return HttpResponse(str(result))
