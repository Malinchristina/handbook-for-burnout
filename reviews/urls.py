from django.urls import path
from .views import (
     ReviewsView,
     AddReview,

)


urlpatterns = [
     path('activity/<int:pk>/reviews/', ReviewsView.as_view(),
          name='activity_reviews'),
    path('activity/<int:pk>/add_review/', AddReview.as_view(), 
         name='add_review'),
    
]
