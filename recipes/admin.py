from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient
# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'menu_type', 'calories']
    inlines = [
        RecipeIngredientInline,
    ]


admin.site.register(Ingredient)
