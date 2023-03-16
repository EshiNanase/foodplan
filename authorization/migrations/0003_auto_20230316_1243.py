# Generated by Django 3.2.12 on 2023-03-16 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_customuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='active_tariff',
            field=models.BooleanField(default=False, verbose_name='Активный тариф'),
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.BooleanField(verbose_name='Включены завтраки')),
                ('lunch', models.BooleanField(verbose_name='Включены обеды')),
                ('dinner', models.BooleanField(verbose_name='Включены ужины')),
                ('desert', models.BooleanField(verbose_name='Включены десерты')),
                ('persons', models.PositiveIntegerField(verbose_name='Количество персон')),
                ('fish_allergy', models.BooleanField(verbose_name='Аллергия на рыбу')),
                ('meat_allergy', models.BooleanField(verbose_name='Аллергия на мясо')),
                ('seed_allergy', models.BooleanField(verbose_name='Аллергия на зерна')),
                ('bee_allergy', models.BooleanField(verbose_name='Аллергия на пчел')),
                ('nut_allergy', models.BooleanField(verbose_name='Аллергия на орехи и бобовые')),
                ('lactose_allergy', models.BooleanField(verbose_name='Аллергия на лактозу')),
                ('end_at', models.DateField(default=django.utils.timezone.now, verbose_name='Заканчивается')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
