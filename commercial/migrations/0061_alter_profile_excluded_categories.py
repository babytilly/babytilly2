# Generated by Django 3.2.25 on 2024-04-21 13:44

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0060_profile_excluded_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='excluded_categories',
            field=models.ManyToManyField(limit_choices_to=models.Q(('departament_id', django.db.models.expressions.F('profile.departament_id'))), to='commercial.CategoryProperties', verbose_name='excluded categories'),
        ),
    ]
