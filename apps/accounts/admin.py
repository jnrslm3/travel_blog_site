from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'avatar',
        'age',
        'city',
        'male',
        'phone',
        'created_at',
        'bio',
    ]
    list_filter = ['created_at', 'city', 'male']
    search_fields = ['username', 'email', 'phone']
