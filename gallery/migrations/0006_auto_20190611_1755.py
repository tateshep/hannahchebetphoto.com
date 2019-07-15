# Generated by Django 2.2.2 on 2019-06-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20190611_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='collection',
        ),
        migrations.AddField(
            model_name='collection',
            name='images',
            field=models.ManyToManyField(blank=True, to='gallery.Image'),
        ),
    ]