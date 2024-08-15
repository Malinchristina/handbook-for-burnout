from django.urls import path
from .views import (
     ActivitiesView,
     AddActivityView,
     EditActivityView,
     DeleteActivityView,
     routines_view,
     podcasts_view,
     indoor_activities_view,
     outdoor_activities_view,
)


urlpatterns = [
     path('', ActivitiesView.as_view(), name='activities'),
     path('add_activity/', AddActivityView.as_view(), name='add_activity'),
     path('edit_activity/<int:pk>/', EditActivityView.as_view(), name='edit_activity'),
     path('delete_activity/<int:pk>/', DeleteActivityView.as_view(), name='delete_activity'),
     path('routines/', routines_view, name='routines'),
     path('podcasts/', podcasts_view, name='podcasts'),
     path('indoor_activities/', indoor_activities_view, name='indoor_activities'),
     path('outdoor_activities/', outdoor_activities_view, name='outdoor_activities'),
]


