from django.db import models
from authorization.models import Allergen


class Ingredient(models.Model):
    name = models.CharField('Название ингредиента', max_length=255)
    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Игредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    CLASSIC = 'CL'
    LOW_CARB = 'LC'
    VEGETARIAN = 'VG'
    KETO = 'KT'

    MENU_TYPE_CHOICES = (
        (CLASSIC, 'Классическое'),
        (LOW_CARB, 'Низкоуглеводное'),
        (VEGETARIAN, 'Вегетарианское'),
        (KETO, 'Кето')
    )

    MEAL_TIME_CHOICES = (
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
        ('desert', 'Десерт'),
    )

    name = models.CharField('Название рецепта', max_length=255)
    menu_type = models.CharField(
        'Тип меню',
        max_length=2,
        choices=MENU_TYPE_CHOICES
    )
    meal_time = models.CharField(
        'Временной промежуток',
        max_length=9,
        choices=MEAL_TIME_CHOICES,
        default='lunch'
    )

    image = models.ImageField('Фото рецепта', upload_to='static/img')
    short_description = models.CharField('Краткое описание', max_length=255)
    instruction = models.TextField('Способ приготовления')
    calories = models.IntegerField('Калорийность')
    allergens = models.ManyToManyField(
        Allergen,
        related_name='recipes',
        blank=True
    )
    ad = models.BooleanField(
        default=False,
        verbose_name='Рекламный рецепт'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    BY_PIECE = 'PS'
    GRAMS = 'GR'
    MILLILITRES = 'ML'
    TO_TASTE = 'TT'

    INGREDIENT_CHOICE = (
        (BY_PIECE, 'шт.'),
        (GRAMS, 'гр.'),
        (MILLILITRES, 'мл'),
        (TO_TASTE, 'по вкусу')
    )

    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='ингредиент',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    quantity = models.IntegerField(
        'Количество',
    )
    unit = models.CharField(
        'Единица измерения',
        max_length=2,
        choices=INGREDIENT_CHOICE
    )

