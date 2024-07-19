from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.categories, name='categories'),
    path('addcategory/', views.add_category, name='add_category'),
]