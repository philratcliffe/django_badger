from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    job_title = models.CharField(max_length=30)

    def __str__(self):
        return self.email
