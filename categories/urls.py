from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='categories'),
    path('routines/', views.routines_view, name='routines'),
    path('podcasts/', views.podcasts_view, name='podcasts'),
    path('indoor-activities/', views.indoor_activities_view, name='indoor-activities'),
    path('outdoor-activities/', views.outdoor_activities_view, name='outdoor-activities'),
    path('addcategory/', views.add_category, name='add_category'),
]