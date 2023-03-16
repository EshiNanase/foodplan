from django.shortcuts import render, get_object_or_404
from .models import Recipe


def get_recipe_details(recipe):
    recipe_items = recipe.ingredients.all()

    ingredients = [{
        'ingredient': item.ingredient,
        'quantity': item.quantity,
        'unit': item.get_unit_display()
    } for item in recipe_items]

    recipe_details = {
        'name': recipe.name,
        'ingredients': ingredients,
        'calories': recipe.calories,
        'description': recipe.short_description,
        'instruction': recipe.instruction
    }
    return {'recipe_details': recipe_details}


def show_recipe_card1(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'card1.html', context=get_recipe_details(recipe))


def show_recipe_card2(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'card2.html', context=get_recipe_details(recipe))

def show_recipe_card3(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'card3.html', context=get_recipe_details(recipe))