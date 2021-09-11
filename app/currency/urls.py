from currency.views import (IndexView, RateListView, RateCreateView,
                            RateDetailView, RateUpdateView, RateDeleteView,
                            )


from django.urls import path

app_name = 'currency'

urlpatterns = [

    path('', IndexView.as_view()),

    #Rate
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

]
