# Generated by Django 4.0.6 on 2022-07-31 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
