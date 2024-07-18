from django.urls import path
from .import views


urlpatterns = [
    path('', views.categories, name='categories'),
    path('addcategory/', views.add_category, name='add_category'),
]