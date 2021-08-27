from currency.views import contact_us, generate_password, hello_world

from django.contrib import admin

from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),


    path('hello-world/', hello_world),
    path('gen-pass/', generate_password),
    path('cont-us/', contact_us),
]
