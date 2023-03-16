from django.contrib import admin
from authorization.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ['email', 'name']

    class Meta:
        model = CustomUser
