from django.db import models
from django.utils import timezone


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)  # privat, monobank
    type = models.CharField(max_length=3)  # USD, EUR
    display_name = models.CharField(max_length=12)


class ContactUs(models.Model):
    created = models.DateTimeField(default=timezone.now())
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    email_form = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=5000)
    email_to = models.EmailField(default='')
    body = models.CharField(max_length=2056, default='')


class Source(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=50)
