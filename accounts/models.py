from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.CharField(max_length=50, null=True)