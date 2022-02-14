# Generated by Django 3.2.11 on 2022-02-03 12:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_alter_event_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dislikes',
            field=models.ManyToManyField(related_name='event_disliked', to=settings.AUTH_USER_MODEL),
        ),
    ]