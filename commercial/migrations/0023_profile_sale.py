# Generated by Django 3.2.9 on 2021-11-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0022_auto_20211129_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sale',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='sale'),
        ),
    ]
