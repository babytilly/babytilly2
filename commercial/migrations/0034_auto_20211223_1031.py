# Generated by Django 3.2.10 on 2021-12-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0033_auto_20211221_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleproperties',
            options={'ordering': ['order', 'name'], 'verbose_name': 'article property', 'verbose_name_plural': 'article properties'},
        ),
        migrations.AddField(
            model_name='articleproperties',
            name='order',
            field=models.PositiveSmallIntegerField(default=1000, verbose_name='article order'),
        ),
    ]