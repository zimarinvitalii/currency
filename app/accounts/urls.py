from django.urls import path
from accounts.views import MyProfileView, SignUpView, ActivateUserView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('my-profile/<int:pk>', MyProfileView.as_view(), name='my-profile'),

    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('activate/<uuid:username>', ActivateUserView.as_view(), name='activate-user'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
