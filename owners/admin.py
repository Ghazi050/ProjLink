from django.contrib import admin
from .models import Project_Owner
from django.contrib.auth.admin import UserAdmin
@admin.register(Project_Owner)
class ProjectOwnerAdmin(admin.ModelAdmin):
    list_display = ('id_owner', 'name_owner', 'Email_owner', 'gender_owner', 'active_owner', 'status_owner', 'Enrolled_Date_owner')
    search_fields = ('name_owner', 'Email_owner', 'phone_owner')
    list_filter = ('gender_owner', 'active_owner', 'status_owner', 'Enrolled_Date_owner')
    ordering = ('Enrolled_Date_owner',)
