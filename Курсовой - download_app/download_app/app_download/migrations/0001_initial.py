# Generated by Django 4.2.7 on 2023-12-18 21:33

import app_download.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('path', models.FileField(upload_to=app_download.models.update_filename)),
            ],
        ),
    ]
