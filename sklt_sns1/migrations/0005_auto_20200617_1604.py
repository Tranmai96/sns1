# Generated by Django 3.0.7 on 2020-06-17 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklt_sns1', '0004_auto_20200615_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]
