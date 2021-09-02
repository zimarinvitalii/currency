from currency.views import contact_us, generate_password, index, rate_list, response_codes, tables

from django.contrib import admin

from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),


    path('index/', index),
    path('gen-pass/', generate_password),
    path('contact-us/', contact_us),
    path('rate/list/', rate_list),
    path('response-codes/', response_codes),
    path('tables', tables),
]
