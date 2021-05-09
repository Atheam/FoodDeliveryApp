# Generated by Django 3.1.7 on 2021-05-03 16:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20210425_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingrestaurants',
            name='close_time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 3, 16, 37, 9, 779897, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pendingrestaurants',
            name='open_time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 3, 16, 37, 9, 779862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='close_time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 3, 16, 37, 9, 779066, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='open_time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 3, 16, 37, 9, 779021, tzinfo=utc)),
        ),
    ]
