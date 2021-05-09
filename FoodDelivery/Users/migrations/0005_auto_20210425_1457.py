# Generated by Django 3.1.7 on 2021-04-25 14:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20210425_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='close_time',
            field=models.TimeField(default=datetime.datetime(2021, 4, 25, 14, 57, 0, 430410, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='open_time',
            field=models.TimeField(default=datetime.datetime(2021, 4, 25, 14, 57, 0, 430383, tzinfo=utc)),
        ),
    ]