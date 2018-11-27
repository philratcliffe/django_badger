from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
from django.db import models

class Badge(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Employee(TimeStampedModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    badges = models.ManyToManyField(Badge, blank=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify("{} {} {}".format(self.first_name, self.last_name, self.pk))
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ["last_name"]
