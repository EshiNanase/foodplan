# Generated by Django 3.2.12 on 2023-03-16 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0009_alter_tariff_ends_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='ends_at',
            field=models.DateField(default=datetime.datetime(2023, 4, 16, 14, 52, 2, 547432), verbose_name='Заканчивается'),
        ),
    ]