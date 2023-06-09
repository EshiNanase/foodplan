# Generated by Django 4.1.7 on 2023-03-17 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0014_alter_customuser_tariff_ends_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tariff',
            name='breakfast',
        ),
        migrations.RemoveField(
            model_name='tariff',
            name='desert',
        ),
        migrations.RemoveField(
            model_name='tariff',
            name='dinner',
        ),
        migrations.RemoveField(
            model_name='tariff',
            name='lunch',
        ),
        migrations.AddField(
            model_name='tariff',
            name='number_of_meals',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество приёмов пищи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tariff_ends_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 16, 14, 4, 30, 76159), verbose_name='Тариф заканчивается'),
        ),
    ]
