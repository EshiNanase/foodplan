# Generated by Django 3.2.12 on 2023-03-18 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0019_auto_20230318_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocode',
            name='discount',
            field=models.PositiveIntegerField(default=100, verbose_name='Размер скидки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tariff',
            name='price',
            field=models.PositiveIntegerField(default=100, verbose_name='Стоимость'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tariff_ends_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 17, 12, 33, 22, 254264), verbose_name='Тариф заканчивается'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='bee_allergy',
            field=models.BooleanField(blank=True, null=True, verbose_name='Продукты пчеловодства'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='breakfast',
            field=models.BooleanField(blank=True, null=True, verbose_name='Включены завтраки'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='desert',
            field=models.BooleanField(blank=True, null=True, verbose_name='Включены десерты'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='dinner',
            field=models.BooleanField(blank=True, null=True, verbose_name='Включены ужины'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='fish_allergy',
            field=models.BooleanField(blank=True, null=True, verbose_name='Рыба и морепродукты'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='lactose_allergy',
            field=models.BooleanField(blank=True, null=True, verbose_name='Молочные продукты '),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='lunch',
            field=models.BooleanField(blank=True, null=True, verbose_name='Включены обеды'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='meat_allergy',
            field=models.BooleanField(blank=True, null=True, verbose_name='Мясо'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='nut_allergy',
            field=models.BooleanField(blank=True, null=True, verbose_name='Орехи и бобовые'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='persons',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество персон'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='seed_allergy',
            field=models.BooleanField(blank=True, null=True, verbose_name='Зерновые'),
        ),
    ]
