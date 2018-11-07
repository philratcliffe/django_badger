from django.db import models

class Employee(models.TimeStampedModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    badge = models.ManyToManyField(Badge)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Badge(models.TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

