# Generated by Django 2.1.3 on 2018-11-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='badges',
            field=models.ManyToManyField(blank=True, to='badger.Badge'),
        ),
    ]
