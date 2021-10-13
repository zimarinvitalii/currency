from django.contrib import admin
from currency.models import Rate, Source, ContactUs

from rangefilter.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin

from currency.resources import RateResource, SourceResource, ContactUsResource


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )

    list_filter = (
        'type',
        'source',
        ('created', DateRangeFilter),
    )
    search_fields = (
        'type',
        'source',
    )
    readonly_fields = (
        'sale',
        'buy',
    )

    def has_delete_permission(self, request, obj=None):
        return False


class SourceAdmin(ImportExportModelAdmin):
    resource_class = SourceResource
    list_display = (
        'id',
        'source_url',
        'name',
    )


class ContactUsAdmin(ImportExportModelAdmin):
    resource_class = ContactUsResource
    list_display = (
        'id',
        'email_to',
        'email_form',
        'subject',
        'body',
        'message',
        'created',
    )
    readonly_fields = (
        'id',
        'email_to',
        'email_form',
        'subject',
        'body',
        'message',
        'created',
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
