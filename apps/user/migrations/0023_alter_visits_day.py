# Generated by Django 4.0.6 on 2022-08-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_user_email_alter_visits_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='day',
            field=models.DateField(auto_now_add=True),
        ),
    ]