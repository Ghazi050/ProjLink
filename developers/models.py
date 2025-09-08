from django.db import models
from datetime import datetime
class Developer(models.Model):
    id_dev = models.IntegerField(null=False, primary_key=True, default=0)
    name_dev = models.CharField(null=False, max_length=40)
    email_dev = models.EmailField(max_length=50, null=False, unique=True)
    is_google_user = models.BooleanField(default=False)
    enrolled_date_dev = models.DateTimeField(default=datetime.now, verbose_name='Year Joined')
    gender_dev = models.CharField(max_length=1)
    active_dev = models.BooleanField(default=True)
    phone_dev = models.CharField(max_length=10, blank=True)
    profile_picture_dev = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    status_dev = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('not_active', 'Not Active'),
        ],
        default='active'
    )
    skills = models.CharField(max_length=300)

    projects = models.ManyToManyField(
        'owners.Project_Owner',
        through='main.Registration',
        related_name='developers'
    )

    def __str__(self):
        return self.name_dev

    def save(self, *args, **kwargs):
        if self.name_dev:
            self.name_dev = self.name_dev.capitalize()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Developer'
        ordering = ['enrolled_date_dev']
