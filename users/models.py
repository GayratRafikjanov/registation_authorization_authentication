from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.html import strip_tags

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=66)
    first_name = models.CharField(max_length=66)
    last_name = models.CharField(max_length=66)
    address1 = models.CharField(max_length=66, blank=True, null=True)
    address2 = models.CharField(max_length=66, blank=True, null=True)
