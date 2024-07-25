from django.urls import path
from . import views

urlpatterns = [
    path('addactivity/', views.add_activity, name='add_activity'), 
    path('routines/', views.routines_view, name='routines'),
    path('podcasts/', views.podcasts_view, name='podcasts'),
    path('indoor-activities/', views.indoor_activities_view, name='indoor-activities'),
    path('outdoor-activities/', views.outdoor_activities_view, name='outdoor-activities'),
]
