from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import AddActivityForm
from .models import AddActivity
from categories.models import AddCategory


def is_staff_or_superuser(user):
    return user.is_staff or user.is_superuser


def not_staff_or_superuser(request):
    return render(request, '403.html')


class ActivitiesView(ListView):
    model = AddActivity
    template_name = 'activities/activities.html'
    context_object_name = 'activities'
    ordering = ['-date_posted']
    paginate_by = 5


class AddActivityView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = AddActivity
    form_class = AddActivityForm
    template_name = 'activities/add_activity.html'
    success_url = reverse_lazy('activities:activities')

    def test_func(self):
        return is_staff_or_superuser(self.request.user)

    def handle_no_permission(self):
        return not_staff_or_superuser(self.request)

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Activity Added Successfully')
        return super().form_valid(form)

    
class EditActivityView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AddActivity
    form_class = AddActivityForm
    template_name = 'activities/edit_activity.html'
    success_url = reverse_lazy('activities:activities')

    def test_func(self):
        return is_staff_or_superuser(self.request.user)

    def handle_no_permission(self):
        return not_staff_or_superuser(self.request)

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Activity Updated Successfully')
        return super().form_valid(form)


class DeleteActivityView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AddActivity
    template_name = 'activities/delete_activity.html'
    success_url = reverse_lazy('activities:activities')

    def test_func(self):
        return is_staff_or_superuser(self.request.user)

    def handle_no_permission(self):
        return not_staff_or_superuser(self.request)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Activity Deleted Successfully')
        return super().delete(request, *args, **kwargs)


def routines_view(request):
    category = get_object_or_404(AddCategory, category_name='Routines')
    activities = AddActivity.objects.filter(
        category=category).annotate(review_count=Count('reviews'))
    return render(request, 'activities/routines.html', {
        'activities': activities,
        'category_name': category.category_name,
        'page_specific_content': 'Routines'
    })


def podcasts_view(request):
    category = get_object_or_404(AddCategory, category_name='Podcasts')
    activities = AddActivity.objects.filter(
        category=category).annotate(review_count=Count('reviews'))
    return render(request, 'activities/podcasts.html', {
        'activities': activities,
        'category_name': category.category_name,
        'page_specific_content': 'Podcasts'
    })


def indoor_activities_view(request):
    category = get_object_or_404(
        AddCategory, category_name='Indoor activities')
    activities = AddActivity.objects.filter(
        category=category).annotate(review_count=Count('reviews'))
    return render(request, 'activities/indoor_activities.html', {
        'activities': activities,
        'category_name': category.category_name,
        'page_specific_content': 'Indoor activities'
    })


def outdoor_activities_view(request):
    category = get_object_or_404(
        AddCategory, category_name='Outdoor activities')
    activities = AddActivity.objects.filter(
        category=category).annotate(review_count=Count('reviews'))
    return render(request, 'activities/outdoor_activities.html', {
        'activities': activities,
        'category_name': category.category_name,
        'page_specific_content': 'Outdoor activities'
    })
