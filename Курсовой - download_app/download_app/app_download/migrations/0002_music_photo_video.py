# Generated by Django 4.2.7 on 2023-12-19 03:11

import app_download.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_download', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('path', models.FileField(upload_to=app_download.models.update_musicname)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('path', models.FileField(upload_to=app_download.models.update_photoname)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('path', models.FileField(upload_to=app_download.models.update_videoname)),
            ],
        ),
    ]
