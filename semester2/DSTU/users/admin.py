from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser

# Register your models here.
UserAdmin.fieldsets += (
    ('Extra Fields', {
        'fields': ('bio', 'phone', 'email')})
)

admin.site.register(MyUser, UserAdmin)
