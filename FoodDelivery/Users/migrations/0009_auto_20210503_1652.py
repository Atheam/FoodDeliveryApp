# Generated by Django 3.1.7 on 2021-05-03 16:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_auto_20210503_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingrestaurants',
            name='close_time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 3, 16, 52, 14, 555930, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pendingrestaurants',
            name='open_time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 3, 16, 52, 14, 555903, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='close_time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 3, 16, 52, 14, 555376, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='open_time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 3, 16, 52, 14, 555338, tzinfo=utc)),
        ),
    ]
