from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'date_joined',)
    search_fields = ('username', 'email',)
    list_filter = ('date_joined',)
    empty_value_display = '-empty-'
