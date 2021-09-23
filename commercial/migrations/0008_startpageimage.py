# Generated by Django 3.2.7 on 2021-09-23 15:10

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0007_delete_startpageimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartPageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='upload/departament/', verbose_name='image')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commercial.departament')),
                ('start_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='commercial.startpage', verbose_name='image')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
    ]
