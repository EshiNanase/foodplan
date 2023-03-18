# Generated by Django 4.1.7 on 2023-03-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0020_alter_customuser_tariff_ends_at_and_more'),
        ('recipes', '0009_recipe_allergens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='allergens',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='authorization.allergen'),
        ),
    ]