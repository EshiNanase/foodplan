from django.shortcuts import render, get_object_or_404
from .models import Recipe
from authorization.models import Tariff


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
        'instruction': recipe.instruction
    }}


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

    filter_args = {
        "meal_time__in": meal_times_filtered
    }
    recipes = [get_recipe_details(recipe) for recipe in Recipe.objects.filter(**filter_args)]
    return render(request, 'card3.html', context={'recipes': recipes})