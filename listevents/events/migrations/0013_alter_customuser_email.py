# Generated by Django 4.0.1 on 2022-01-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_remove_customuser_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
