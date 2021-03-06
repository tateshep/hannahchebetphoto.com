# Generated by Django 2.2.2 on 2019-06-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_remove_image_file_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.RemoveField(
            model_name='image',
            name='collection',
        ),
        migrations.AddField(
            model_name='image',
            name='collection',
            field=models.ManyToManyField(blank=True, to='gallery.Collection'),
        ),
    ]
