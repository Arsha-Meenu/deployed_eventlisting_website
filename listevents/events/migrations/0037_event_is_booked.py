# Generated by Django 3.2.11 on 2022-02-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0036_auto_20220213_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_booked',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
