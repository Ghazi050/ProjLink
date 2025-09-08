# developers/admin.py
from django.contrib import admin
from .models import Developer

class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        'id_dev',
        'name_dev',
        'email_dev',
        'gender_dev',
        'status_dev',
        'active_dev',
        'enrolled_date_dev',
    )
    list_filter = (
        'active_dev',
        'status_dev',
        'enrolled_date_dev',
    )
    ordering = ('enrolled_date_dev',)

# تسجيل موديل Developer في لوحة الإدارة
admin.site.register(Developer, DeveloperAdmin)
