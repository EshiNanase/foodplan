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
from recipes.views import show_recipe_card1, show_recipe_card2, show_recipe_card3
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='home_page'),
    path('admin/', admin.site.urls),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('profile', profile_view, name='profile'),
    path('order', order_view, name='order'),
    path('card1/<int:recipe_id>', show_recipe_card1, name='show_recipe_card1'),
    path('card2/<int:recipe_id>', show_recipe_card2, name='show_recipe_card2'),
    path('card3/<int:recipe_id>', show_recipe_card3, name='show_recipe_card3'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
