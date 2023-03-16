"""foodplan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authorization.views import IndexView, LoginView, RegistrationView
from recipes.views import show_recipe_card1, show_recipe_card2, show_recipe_card3

urlpatterns = [
    path('', IndexView.as_view(), name='home_page'),
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegistrationView.as_view(), name='register'),
    path('card1/<int:recipe_id>', show_recipe_card1, name='show_recipe_card1'),
    path('card2/<int:recipe_id>', show_recipe_card2, name='show_recipe_card2'),
    path('card3/<int:recipe_id>', show_recipe_card3, name='show_recipe_card3'),
]
