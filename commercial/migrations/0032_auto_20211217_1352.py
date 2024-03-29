# Generated by Django 3.2.10 on 2021-12-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0031_auto_20211213_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='additional_emails',
            field=models.CharField(blank=True, default='', help_text='Enter multiple mailboxes separated by commas', max_length=128, verbose_name='additional email addresses'),
        ),
        migrations.AlterField(
            model_name='articleproperties',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10, verbose_name='volume'),
        ),
        migrations.AlterField(
            model_name='articleproperties',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10, verbose_name='weight'),
        ),
    ]
