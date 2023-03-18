from django.contrib import admin
from authorization.models import CustomUser, Tariff, Allergen


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    class Meta:
        model = Tariff


class TariffInline(admin.TabularInline):
    model = Tariff
    extra = 0


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ['email', 'name', 'tariff_ends_at']
    inlines = [TariffInline]

    class Meta:
        model = CustomUser

admin.site.register(Allergen)