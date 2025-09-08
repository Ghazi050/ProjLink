from django.db import models
from datetime import datetime

class Project_Owner(models.Model):
    id_owner = models.IntegerField(null=False, primary_key=True,default=0)
    name_owner = models.CharField(null=False, max_length=40)
    Email_owner = models.EmailField(max_length=50, null=False, unique=True)
    is_google_user = models.BooleanField(default=False)
    Enrolled_Date_owner = models.DateTimeField(default=datetime.now, verbose_name='Year Joined')
    gender_owner = models.CharField(max_length=1)
    active_owner = models.BooleanField(default=True)
    phone_owner = models.CharField(max_length=10, blank=True)
    profile_picture_owner = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    status_owner = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('not_active', 'Not Active'),
        ],
        default='active'
    )

    def __str__(self):
        return self.name_owner

    def save(self, *args, **kwargs):
        if self.name_owner:
            self.name_owner = self.name_owner.capitalize()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Project Owner'
        ordering = ['Enrolled_Date_owner']

