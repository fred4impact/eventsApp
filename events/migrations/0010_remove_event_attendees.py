# Generated by Django 4.2.2 on 2023-06-22 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_event_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendees',
        ),
    ]
