from currency.views import (contact_us, generate_password, index,
                            rate_list, response_codes, rate_create,
                            rate_details, rate_update, rate_delete,
                            source_list, source_create, source_update, source_delete)

from django.contrib import admin

from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', index),
    path('gen-pass/', generate_password),
    path('contact-us/', contact_us),

    #Rate
    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('rate/details/<int:rate_id>/', rate_details),
    path('rate/update/<int:rate_id>/', rate_update),
    path('rate/delete/<int:rate_id>/', rate_delete),

    path('source/list/', source_list),
    path('source/create/', source_create),
    path('source/update/<int:source_id>/', source_update),
    path('source/delete/<int:source_id>/', source_delete),

    path('response-codes/', response_codes),

]
