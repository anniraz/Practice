# Generated by Django 4.0.6 on 2022-07-30 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_daynumber_visitscount_remove_visits_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visits',
            name='day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
