from import_export import resources

from currency.models import Rate, Source, ContactUs


class RateResource(resources.ModelResource):

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'type',
            'source',
            'created',
        )


class SourceResource(resources.ModelResource):

    class Meta:
        model = Source
        fields = (
            'id',
            'source_url',
            'name',
        )


class ContactUsResource(resources.ModelResource):

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_to',
            'email_form',
            'subject',
            'body',
            'message',
            'created',


        )
