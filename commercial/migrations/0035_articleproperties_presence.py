# Generated by Django 3.2.10 on 2021-12-24 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0034_auto_20211223_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleproperties',
            name='presence',
            field=models.CharField(blank=True, max_length=127, null=True, verbose_name='presence'),
        ),
    ]