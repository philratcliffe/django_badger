# Generated by Django 2.1.3 on 2018-12-24 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='job_description',
            new_name='job_title',
        ),
    ]
