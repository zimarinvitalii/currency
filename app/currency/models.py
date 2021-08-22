from django.db import models


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)  # privat, monobank
    type = models.CharField(max_length=3)  # USD, EUR
    display_name = models.CharField(max_length=12)

class ContactUs(models.Model):
    email_form = models.CharField(max_length=50)

