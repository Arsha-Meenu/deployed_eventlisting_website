# Generated by Django 3.2.11 on 2022-02-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0040_auto_20220214_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/media'),
        ),
    ]
