import itertools
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
from django.db import models
from .validators import validate_employee_name


class Badge(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        for x in itertools.count(1):
            if not Employee.objects.filter(slug=slug).exists():
                break
            slug = '%s-%d' % (slug, x)
        self.slug = slug
        super(Badge, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Employee(TimeStampedModel):
    first_name = models.CharField(
        max_length=30, validators=[validate_employee_name])
    last_name = models.CharField(
        max_length=30, validators=[validate_employee_name])
    badges = models.ManyToManyField(Badge, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        slug = slugify("{} {}".format(self.first_name, self.last_name))
        for x in itertools.count(1):
            if not Employee.objects.filter(slug=slug).exists():
                break
            slug = '%s-%d' % (slug, x)
        self.slug = slug
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ["last_name"]
