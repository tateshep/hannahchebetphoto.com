# Generated by Django 2.2.2 on 2019-06-11 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20190611_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]