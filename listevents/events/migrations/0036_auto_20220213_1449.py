# Generated by Django 3.2.11 on 2022-02-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0035_merge_20220213_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]