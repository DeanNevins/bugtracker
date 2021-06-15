from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Employee(AbstractUser):
    displayname = models.CharField(max_length=30)
    position = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.displayname:
            return self.displayname
        else:
            return self.username