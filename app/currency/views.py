from django.urls import reverse, reverse_lazy
from currency.tasks import contact_us
from django.http import HttpResponse, HttpResponseRedirect

from currency.utils import generate_password as gen_pass

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.views.generic import (
    ListView, CreateView, DetailView,
    UpdateView, DeleteView, View, TemplateView)

from django.shortcuts import render, get_object_or_404


# def index(request):
#     return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'


# def generate_password(request):
#     password_len = int(request.GET.get('password-len'))
#     password = gen_pass(password_len)
#     return HttpResponse(password)


# class GeneratePasswordView(View):
#     def get(self, request):
#         password_len = int(request.GET.get('password-len'))
#         password = gen_pass(password_len)
#         return HttpResponse(password)
#


class GeneratePasswordView(TemplateView):
    template_name = 'generate_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        password_len = int(self.request.GET.get('password-len'))
        context['password'] = gen_pass(password_len)
        return context


# def rate_list(request):
#     rates = Rate.objects.all()
#     context = {
#         'rate_list': rates,
#     }
#
#     return render(request, 'rate_list.html', context=context)


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class ContactUsCreateView(CreateView):
    model = ContactUs
    success_url = reverse_lazy('index')
    template_name = 'contact_us_create.html'
    fields = (
        'email_to',
        'subject',
        'body',
    )

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        body = form.cleaned_data['body']
        email_to = form.cleaned_data['email_to']

        full_email_body = f'''
        Email from: {email_to}
        Body: {body}
        '''



        contact_us.apply_async(args=(subject, ), kwargs={'body': full_email_body})

        return super().form_valid(form)

    def form_invalid(self, form):
        print('form_invalid')
        return super().form_invalid(form)


# def rate_create(request):
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list/')
#     elif request.method == 'GET':
#         form = RateForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'rate_create.html', context=context)


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class ContactUsView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_us.html'


# def contact_us(request):
#     contacts = ContactUs.objects.all()
#     context = {
#         'contact_us': contacts,
#     }
#
#     return render(request, 'contact_us.html', context=context)


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


# def rate_details(request, rate_id):
#     """
#     try:
#         rate = Rate.objects.get(id=rate_id)
#     except Rate.DoesNotExist as exc:
#         raise Http404(exc)
#     """
#     rate = get_object_or_404(Rate, id=rate_id)
#     context = {
#         'object': rate,
#     }
#     return render(request, 'rate_details.html', context=context)

class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


# def rate_update(request, rate_id):
#     rate = get_object_or_404(Rate, id=rate_id)
#
#     if request.method == 'POST':
#         form = RateForm(request.POST, instance=rate)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list/')
#     elif request.method == 'GET':
#         form = RateForm(instance=rate)
#     context = {
#         'form': form,
#     }
#     return render(request, 'rate_update.html', context=context)


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


# def rate_delete(request, rate_id):
#     rate = get_object_or_404(Rate, id=rate_id)
#
#     if request.method == 'POST':
#         rate.delete()
#         return HttpResponseRedirect('/rate/list/')
#
#     # if request.method == 'GET'
#     context = {
#         'object': rate,
#     }
#     return render(request, 'rate_delete.html', context=context)


# Source
class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


# def source_list(request):
#     sources = Source.objects.all()
#     context = {
#         'source_list': sources,
#     }
#     return render(request, 'source_list.html', context=context)


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_create.html'


# def source_create(request):
#     if request.method == 'POST':
#         form = SourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/list/')
#     elif request.method == 'GET':
#         form = SourceForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'source_create.html', context=context)

class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_update.html'


# def source_update(request, source_id):
#     source = get_object_or_404(Source, id=source_id)
#
#     if request.method == 'POST':
#         form = SourceForm(request.POST, instance=source)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/list/')
#     elif request.method == 'GET':
#         form = SourceForm(instance=source)
#     context = {
#         'form': form,
#     }
#     return render(request, 'source_update.html', context=context)

class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_delete.html'


# def source_delete(request, source_id):
#     source = get_object_or_404(Source, id=source_id)
#
#     if request.method == 'POST':
#         source.delete()
#         return HttpResponseRedirect('/source/list/')
#
#     # if request.method == 'GET'
#     context = {
#         'object': source,
#     }
#     return render(request, 'source_delete.html', context=context)


def response_codes(request):
    response = HttpResponse('Response', status=301, headers={'Location': 'https://google.com'})
    return response
