# Generated by Django 4.1 on 2022-08-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='science',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sciences/images'),
        ),
    ]
