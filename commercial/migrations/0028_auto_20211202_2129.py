# Generated by Django 3.2.9 on 2021-12-02 21:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0027_clear_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sale',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='sale in %'),
        ),
        migrations.CreateModel(
            name='DepartamentSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sum', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='order sum')),
                ('sale', models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='sale in %')),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commercial.departament', verbose_name='departament')),
            ],
            options={
                'verbose_name': 'departament sale',
                'verbose_name_plural': 'departament sales',
                'ordering': ['-order_sum'],
            },
        ),
        migrations.AddConstraint(
            model_name='departamentsale',
            constraint=models.UniqueConstraint(fields=('departament', 'order_sum', 'sale'), name='unique_departament_order_sum_sale'),
        ),
    ]
