# Generated by Django 3.0 on 2021-10-04 01:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_family_members'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='family',
            name='members',
        ),
        migrations.AddField(
            model_name='family',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
