# Generated by Django 2.0.1 on 2018-01-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region_name',
            name='region_image',
            field=models.ImageField(blank=True, upload_to='reg_images'),
        ),
    ]
