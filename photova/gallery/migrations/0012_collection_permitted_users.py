# Generated by Django 2.2.2 on 2019-06-14 19:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0011_auto_20190614_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='permitted_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
