from django.shortcuts import render, get_object_or_404
from .models import Recipe


def show_recipe_card(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe_items = recipe.ingredients.all()
    ingredients = [{
        'ingredient': item.ingredient,
        'quantity': item.quantity,
        'unit': item.get_unit_display()
    } for item in recipe_items]
    recipe_details = {
        'name': recipe.name,
        'ingredients': ingredients,
        'calories': recipe.calories
    }
    return render(request, 'card.html', context={'recipe_details': recipe_details})
