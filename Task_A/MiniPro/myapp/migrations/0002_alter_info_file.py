# Generated by Django 5.1.7 on 2025-03-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='file',
            field=models.ImageField(upload_to='media/user_files'),
        ),
    ]
