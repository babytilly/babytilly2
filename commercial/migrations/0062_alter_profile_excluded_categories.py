# Generated by Django 3.2.25 on 2024-04-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0061_alter_profile_excluded_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='excluded_categories',
            field=models.ManyToManyField(to='commercial.Category', verbose_name='excluded categories'),
        ),
    ]
