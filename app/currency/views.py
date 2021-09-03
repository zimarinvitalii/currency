from django.http import HttpResponse, HttpResponseRedirect, Http404

from currency.utils import generate_password as gen_pass

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm

from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'index.html')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rate_list': rates,
    }

    return render(request, 'rate_list.html', context=context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()
    context = {
        'form': form,
    }
    return render(request, 'rate_create.html', context=context)


def contact_us(request):
    contacts = ContactUs.objects.all()
    context = {
        'contact_us': contacts,
    }

    return render(request, 'contact_us.html', context=context)


def rate_details(request, rate_id):
    """
    try:
        rate = Rate.objects.get(id=rate_id)
    except Rate.DoesNotExist as exc:
        raise Http404(exc)
    """
    rate = get_object_or_404(Rate, id=rate_id)
    context = {
        'object': rate,
    }
    return render(request, 'rate_details.html', context=context)


def rate_update(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)
    context = {
        'form': form,
    }
    return render(request, 'rate_update.html', context=context)


def rate_delete(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')

    # if request.method == 'GET'
    context = {
        'object': rate,
    }
    return render(request, 'rate_delete.html', context=context)


#Source
def source_list(request):
    sources = Source.objects.all()
    context = {
        'source_list': sources,
    }
    return render(request, 'source_list.html', context=context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        form = SourceForm()
    context = {
        'form': form,
    }
    return render(request, 'source_create.html', context=context)


def source_update(request, source_id):
    source = get_object_or_404(Source, id=source_id)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        form = SourceForm(instance=source)
    context = {
        'form': form,
    }
    return render(request, 'source_update.html', context=context)


def source_delete(request, source_id):
    source = get_object_or_404(Source, id=source_id)

    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/list/')

    # if request.method == 'GET'
    context = {
        'object': source,
    }
    return render(request, 'source_delete.html', context=context)


def response_codes(request):
    response = HttpResponse('Response', status=301, headers={'Location': 'https://google.com'})
    return response

