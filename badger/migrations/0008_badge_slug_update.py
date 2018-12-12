# Generated by Django 2.1.3 on 2018-12-10 10:48

from django.db import migrations, models
from badger.models import Badge


def migrate_data_forward(apps, schema_editor):
    for instance in Badge.objects.all():
        instance.save() # Will trigger slug update
        print("Generated slug {}".format(instance.slug))

def migrate_data_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('badger', '0007_slug_nonull'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.RunPython(migrate_data_forward, migrate_data_backward)
    ]