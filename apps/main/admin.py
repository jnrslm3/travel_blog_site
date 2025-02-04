from django.contrib import admin
# Register your models here.
from .models import ContactUs, Subscription

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
        'text',
        'created_at'
    ]
    list_filter = ['created_at']
    search_fields = ['name',
                     'email',]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    last_display = [
        'email',
    ]