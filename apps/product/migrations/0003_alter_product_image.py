# Generated by Django 4.0.6 on 2022-07-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product/'),
        ),
    ]