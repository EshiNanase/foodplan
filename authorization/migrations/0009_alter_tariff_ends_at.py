# Generated by Django 3.2.12 on 2023-03-16 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0008_auto_20230316_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='ends_at',
            field=models.DateField(default=datetime.datetime(2023, 4, 16, 13, 30, 53, 599169), verbose_name='Заканчивается'),
        ),
    ]
