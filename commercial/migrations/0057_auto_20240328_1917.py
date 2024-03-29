# Generated by Django 3.2.24 on 2024-03-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0056_message_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.IntegerField(choices=[(0, 'opened'), (1, 'closed'), (2, 'in progress'), (3, 'no answer')], default=0, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False, editable=False, verbose_name='is read'),
        ),
    ]