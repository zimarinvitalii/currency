from django.shortcuts import render
from django.http import HttpResponse

from currency.utils import generate_password as gen_pass
# Create your views here.

def hello_world(request):
    return HttpResponse('Hello World')

def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)

def contact_us(request):
    return HttpResponse('Contact Us')