# Generated by Django 4.0.1 on 2022-01-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_customuser_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
    ]
