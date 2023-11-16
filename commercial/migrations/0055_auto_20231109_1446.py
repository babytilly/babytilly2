# Generated by Django 3.2.23 on 2023-11-09 14:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0054_auto_20231104_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'ordering': ['-id'], 'verbose_name': 'complaint', 'verbose_name_plural': 'complaints'},
        ),
        migrations.AddField(
            model_name='complaint',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date of create'),
            preserve_default=False,
        ),
    ]