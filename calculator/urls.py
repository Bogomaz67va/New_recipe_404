from django.urls import path
from .views import ingredient_views

urlpatterns = [
    path('<recipe_name>/', ingredient_views, name='recipe')
]