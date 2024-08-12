from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import AddActivityForm
from .models import AddActivity
from categories.models import AddCategory


@login_required
@user_passes_test(lambda u: u.is_staff)
def add_activity(request):
    if request.method == 'POST':
        form = AddActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.author = request.user
            activity.save()
            messages.success(request, 'The activity was successfully added.')
            return redirect('categories') 
    else:
        form = AddActivityForm()
    return render(request, 'activities/add_activity.html', {'form': form})

def edit_activity(request, pk):
    activity = get_object_or_404(AddActivity, pk=pk)
    if request.method == 'POST':
        form = AddActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'The activity was successfully updated.')
            return redirect('categories')
    else:
        form = AddActivityForm(instance=activity)
    return render(request, 'activities/edit_activity.html', {'form': form})


def delete_activity(request, pk):
    activity = get_object_or_404(AddActivity, pk=pk)
    activity.delete()
    messages.success(request, 'The activity was successfully deleted.')
    return redirect('categories')


def routines_view(request):
    category = get_object_or_404(AddCategory, category_name='Routines')
    activities = AddActivity.objects.filter(category=category).annotate(review_count=Count('reviews'))
    return render(request, 'activities/routines.html', {
        'activities': activities,
        'category_name': category.category_name,
        'page_specific_content': 'Routines'
    })

def podcasts_view(request):
    category = get_object_or_404(AddCategory, category_name='Podcasts')
    activities = AddActivity.objects.filter(category=category)
    return render(request, 'activities/podcasts.html', {
        'activities': activities,
        'category_name': category.category_name,
        'page_specific_content': 'Podcasts'
    })

def indoor_activities_view(request):
    category = get_object_or_404(AddCategory, category_name='Indoor activities')
    activities = AddActivity.objects.filter(category=category)
    return render(request, 'activities/indoor_activities.html', {
        'activities': activities,
        'category_name': category.category_name,
        'page_specific_content': 'Indoor activities'
    })


def outdoor_activities_view(request):
    category = get_object_or_404(AddCategory, category_name='Outdoor activities')
    activities = AddActivity.objects.filter(category=category)
    return render(request, 'activities/outdoor_activities.html', {
        'activities': activities,
        'category_name': category.category_name,
        'page_specific_content': 'Outdoor activities'
    })
