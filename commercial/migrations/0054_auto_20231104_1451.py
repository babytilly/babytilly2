# Generated by Django 3.2.23 on 2023-11-04 14:51

import sorl.thumbnail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0053_auto_20231104_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='receipt',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='attachment/%Y/%m/%d/%H/%m/', verbose_name='receipt'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.IntegerField(choices=[(0, 'opened'), (1, 'closed'), (2, 'in progress')], default=0, verbose_name='status'),
        ),
    ]
