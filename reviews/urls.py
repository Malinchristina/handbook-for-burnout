from django.urls import path
from .views import (
    add_review, 
    ReviewsView,
    EditReview,
    DeleteReview,
)


urlpatterns = [
    path('add_review/<int:activity_pk>/', add_review,
         name='add_review'),
    path('edit_review/<int:pk>/', EditReview.as_view(),
         name='edit_review'),
    path('delete_review/<int:pk>/', DeleteReview.as_view(),
         name='delete_review'),
    path('activity/<int:pk>/reviews/', ReviewsView.as_view(), 
         name='activity_reviews'),
]
