# Generated by Django 3.2.9 on 2021-11-25 16:33

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0017_articleimage_departament'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AddField(
            model_name='articleproperties',
            name='main_image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='photos/', verbose_name='main image'),
        ),
    ]
