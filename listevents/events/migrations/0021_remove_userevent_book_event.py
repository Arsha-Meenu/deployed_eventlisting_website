# Generated by Django 3.2.11 on 2022-02-02 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_userevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userevent',
            name='book_event',
        ),
    ]
