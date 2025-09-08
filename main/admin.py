from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Registration


# ---------------- Registration -----------------
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('dev', 'owner', 'registration_date')
    search_fields = ('dev__name_dev', 'owner__name_owner')
    list_filter = ('registration_date',)
    ordering = ('-registration_date',)
