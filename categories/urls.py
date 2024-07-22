from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='categories'),
    path('addcategory/', views.add_category, name='add_category'),
]