# Generated by Django 3.2.11 on 2022-02-03 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_remove_userevent_book_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='categories',
            field=models.CharField(choices=[('Under-Graduate', 'Under-Graduate'), ('Post-Graduate', 'Post-Graduate'), ('Doctoralstudies', 'Doctoralstudies'), ('Vocational Education', 'Vocational Education'), ('Distance Education', 'Distance Education')], default='UG', max_length=100),
        ),
    ]
