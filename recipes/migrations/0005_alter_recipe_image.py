# Generated by Django 3.2.12 on 2023-03-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipeingredient_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='static/img', verbose_name='Фото рецепта'),
        ),
    ]
