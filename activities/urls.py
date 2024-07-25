from django.urls import path
from . import views

urlpatterns = [
    path('', views.activities, name='activities'),
    path('addactivity/', views.add_activity, name='add_activity'), 
]
