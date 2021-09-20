# Generated by Django 3.0 on 2021-09-15 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210915_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_families', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
