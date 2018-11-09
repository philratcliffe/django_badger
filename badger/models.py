from model_utils.models import TimeStampedModel
from django.db import models

class Badge(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(TimeStampedModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    badges = models.ManyToManyField(Badge, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

