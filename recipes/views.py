from django.shortcuts import render, get_object_or_404
from .models import Recipe
from authorization.models import Tariff
from django.db.models import Case, When
from django.db import models
from authorization.decorators import tariff_required


@tariff_required
def get_recipe_details(recipe):
    recipe_items = recipe.ingredients.all()

    ingredients = [{
        'ingredient': item.ingredient,
        'quantity': item.quantity,
        'unit': item.get_unit_display()
    } for item in recipe_items]

    return {'recipe_details':{
        'name': recipe.name,
        'ingredients': ingredients,
        'calories': recipe.calories,
        'description': recipe.short_description,
        'instruction': recipe.instruction,
        'meal_time': recipe.get_meal_time_display()
    }}


@tariff_required
def show_tariff_card(request):
    user = request.user
    tariff = Tariff.objects.get(user=user)
    meal_times = {
        'breakfast': tariff.breakfast,
        'lunch': tariff.lunch,
        'dinner': tariff.dinner,
        'desert': tariff.desert
    }

    meal_times_filtered = [key for key, value in meal_times.items() if value]
    allergens = tariff.allergens.all()
    recipes = Recipe.objects.filter(meal_time__in=meal_times_filtered).exclude(allergens__in=allergens)

    unique_recipes = []
    meal_times = set()
    for recipe in recipes.order_by(
    Case(
        When(meal_time='breakfast', then=0),
        When(meal_time='lunch', then=1),
        When(meal_time='dinner', then=2),
        When(meal_time='desert', then=3),
        output_field=models.IntegerField(),
    ),
    'id'
):
        if recipe.meal_time not in meal_times:
            meal_times.add(recipe.meal_time)
            unique_recipes.append(get_recipe_details(recipe))
    return render(request, 'card.html', context={'recipes': unique_recipes})


def show_recipe_card(request, recipe_id):
    recipe = Recipe.objects.get(
        id=recipe_id
    )

    recipe_items = recipe.ingredients.all()

    ingredients = [{
        'ingredient': item.ingredient,
        'quantity': item.quantity,
        'unit': item.get_unit_display()
    } for item in recipe_items]

    conext = {'recipe': {
        'name': recipe.name,
        'ingredients': ingredients,
        'calories': recipe.calories,
        'description': recipe.short_description,
        'instruction': recipe.instruction,
        'meal_time': recipe.get_meal_time_display()
    }}
    return render(request, 'card2.html', context=conext)


def show_recipe2_card(request, recipe_id):
    recipe = Recipe.objects.get(
        id=recipe_id
    )

    recipe_items = recipe.ingredients.all()

    ingredients = [{
        'ingredient': item.ingredient,
        'quantity': item.quantity,
        'unit': item.get_unit_display()
    } for item in recipe_items]

    conext = {'recipe': {
        'name': recipe.name,
        'ingredients': ingredients,
        'calories': recipe.calories,
        'description': recipe.short_description,
        'instruction': recipe.instruction,
        'meal_time': recipe.get_meal_time_display()
    }}
    return render(request, 'card2.html', context=conext)


def show_recipe3_card(request):
    recipe = Recipe.objects.all()[2]

    recipe_items = recipe.ingredients.all()

    ingredients = [{
        'ingredient': item.ingredient,
        'quantity': item.quantity,
        'unit': item.get_unit_display()
    } for item in recipe_items]

    conext = {'recipe': {
        'name': recipe.name,
        'ingredients': ingredients,
        'calories': recipe.calories,
        'description': recipe.short_description,
        'instruction': recipe.instruction,
        'meal_time': recipe.get_meal_time_display()
    }}
    return render(request, 'card2.html', context=conext)
