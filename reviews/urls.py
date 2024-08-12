from django.urls import path
from . import views


urlpatterns = [
    path('<int:activity_pk>/', views.reviews, name='reviews'),
    path('editreview/<int:pk>/', views.EditReview.as_view(),
         name='edit_review'),
    path('deletereview/<int:pk>/', views.delete_review, name='delete_review'),
]
