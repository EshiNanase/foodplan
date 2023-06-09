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
from authorization.views import IndexView, login_view, register_view, profile_view, logout_view, order_view
from recipes.views import show_tariff_card, show_ad_recipe_card
from django.conf import settings
from django.conf.urls.static import static
from authorization.payment import stripe_webhook_view

urlpatterns = [
    path('', IndexView.as_view(), name='home_page'),
    path('admin/', admin.site.urls),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('profile', profile_view, name='profile'),
    path('order', order_view, name='order'),
    path('tariff_card', show_tariff_card, name='tariff_card'),
    path('webhook', stripe_webhook_view, name='stripe_webhook'),
    path('recipe/<int:recipe_id>', show_ad_recipe_card, name='ad_recipe'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
