# Generated by Django 3.2.12 on 2023-03-16 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0011_auto_20230316_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tariff',
            name='ends_at',
        ),
        migrations.AddField(
            model_name='customuser',
            name='tariff_ends_at',
            field=models.DateField(default=datetime.datetime(2023, 4, 16, 15, 32, 30, 887620), verbose_name='Тариф заканчивается'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='bee_allergy',
            field=models.BooleanField(verbose_name='Пчелы'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='fish_allergy',
            field=models.BooleanField(verbose_name='Рыба'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='lactose_allergy',
            field=models.BooleanField(verbose_name='Лактоза'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='meat_allergy',
            field=models.BooleanField(verbose_name='Мясо'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='nut_allergy',
            field=models.BooleanField(verbose_name='Орехи и бобовые'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='seed_allergy',
            field=models.BooleanField(verbose_name='Зерно'),
        ),
    ]
