from django.db import models


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

    name = models.CharField('Название рецепта', max_length=255)
    menu_type = models.CharField(
        'Тип меню',
        max_length=2,
        choices=MENU_TYPE_CHOICES
    )
    image = models.ImageField('Фото рецепта', upload_to='static/img')
    short_description = models.CharField('Краткое описание', max_length=255)
    instruction = models.TextField('Способ приготовления')
    calories = models.IntegerField('Калорийность')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    BY_PIECE = 'P'
    IN_GRAMS = 'G'

    INGREDIENT_CHOICE = (
        (BY_PIECE, 'штук'),
        (IN_GRAMS, 'граммов')
    )

    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='ингредиент',
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE
    )
    quantity = models.DecimalField(
        'Количество',
        max_digits=6,
        decimal_places=2
    )
    unit = models.CharField(
        'Единица измерения',
        max_length=1,
        choices=INGREDIENT_CHOICE
    )

