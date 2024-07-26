from reviews.views import reviews
from django.urls import path

urlpatterns = [
    path('reviews/', reviews, name='reviews'),
]