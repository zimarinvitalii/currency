from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, RedirectView
# Create your views here.
from accounts.forms import SignUpForm
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    fields = (
        'first_name',
        'last_name',
    )
    success_url = reverse_lazy('index')
    template_name = 'my_profile.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)
    #     return queryset

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(CreateView):
    model = User
    template_name = 'sign_up.html'
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class ActivateUserView(RedirectView):
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        user = get_object_or_404(User, username=username, is_active=False)

        user.is_active = True

        # update_fields - save only needed(minimum) fields
        user.save(update_fields=('is_active', ))

        return super().get_redirect_url(*args, **kwargs)


