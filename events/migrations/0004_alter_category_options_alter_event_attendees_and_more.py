# Generated by Django 4.2 on 2023-05-11 21:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_category_remove_event_end_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(null=True, related_name='registered_event', through='events.Registration', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
