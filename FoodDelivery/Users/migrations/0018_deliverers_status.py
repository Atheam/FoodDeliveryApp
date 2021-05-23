# Generated by Django 3.1.7 on 2021-05-23 02:36

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0017_remove_deliverers_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverers',
            name='status',
            field=models.CharField(choices=[('NOTAVAILABLE', 'Unavailable'), ('AVAILABLE', 'Available'), ('BUSY', 'Busy')], default=Users.models.DelivererStatus['NOTAVAILABLE'], max_length=16),
        ),
    ]
