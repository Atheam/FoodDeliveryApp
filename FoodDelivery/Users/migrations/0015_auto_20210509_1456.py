# Generated by Django 3.1.7 on 2021-05-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0014_deliverers_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverers',
            name='latitude',
            field=models.CharField(default='0.0', max_length=100),
        ),
        migrations.AddField(
            model_name='deliverers',
            name='longitude',
            field=models.CharField(default='0.0', max_length=100),
        ),
    ]