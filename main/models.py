from django.db import models
from developers.models import Developer
from owners.models import Project_Owner
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    is_owner = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Registration(models.Model):
    dev = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Project_Owner, on_delete=models.SET_NULL, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('dev', 'owner')
