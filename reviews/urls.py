from django.urls import path
from . import views


urlpatterns = [
    path('<int:activity_pk>/', views.reviews, name='reviews'),
]