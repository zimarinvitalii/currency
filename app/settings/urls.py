from currency.views import (ContactUsView,  GeneratePasswordView, IndexView,
                            response_codes, SourceListView, SourceCreateView,
                            SourceUpdateView, SourceDeleteView)

from django.contrib import admin
import debug_toolbar
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),


    path('silk/', include('silk.urls', namespace='silk')),



    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),

    path('auth/', include('django.contrib.auth.urls')),


    path('index/', IndexView.as_view(), name='index'),
    path('gen-pass/',  GeneratePasswordView.as_view()),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),


    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),

    path('response-codes/', response_codes),

    path('__debug__/', include(debug_toolbar.urls)),
]
