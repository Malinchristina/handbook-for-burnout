from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from activities.models import AddActivity


# Create your views here.

def handle_no_permission(request):
    return render(request, '403.html')


class ReviewsView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'
    ordering = ['-created_on']
    paginate_by = 5

    def get_queryset(self):
        activity_pk = self.kwargs.get('pk')
        activity = get_object_or_404(AddActivity, pk=activity_pk)
        return Review.objects.filter(activity_pk=activity)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity_pk = self.kwargs.get('pk')
        activity = get_object_or_404(AddActivity, pk=activity_pk)
        form = ReviewForm()
        context['activity_name'] = activity.activity_name
        context['activity'] = activity
        context['form'] = form
        return context

    
class AddReview(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/reviews.html'

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        activity_pk = self.kwargs.get('pk')
        activity = get_object_or_404(AddActivity, pk=activity_pk)
        form.instance.author = self.request.user
        form.instance.activity_pk = activity
        response = super().form_valid(form)
        messages.success(self.request, 'Review Added Successfully')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('activity_reviews', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity_pk = self.kwargs.get('pk')
        activity = get_object_or_404(AddActivity, pk=activity_pk)
        context['activity_name'] = activity.activity_name
        context['activity_pk'] = activity_pk
        context['activity'] = activity
        return context

    
# class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Review
#     form_class = ReviewForm
#     template_name = 'reviews/edit_reviews.html'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         messages.success(self.request, 'Review Updated Successfully')
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('activity_reviews', kwargs={'pk': self.kwargs['pk']})

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         activity_pk = self.kwargs.get('pk')
#         activity = get_object_or_404(AddActivity, pk=activity_pk)
#         context['activity_name'] = activity.activity_name
#         context['activity_pk'] = activity_pk
#         context['activity'] = activity
#         context['form'] = self.get_form()
#         return context


class EditReview(UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/edit_reviews.html'

    def get_success_url(self):
        return reverse_lazy('activity_reviews', kwargs={
            'pk': self.object.activity_pk.pk})

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

    def form_valid(self, form):
        self.object = form.save()
        messages.success(
        self.request, 'Your review was successfully updated.')
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request,
        'There was an error updating your review.')
        return self.render_to_response(self.get_context_data(form=form))

    def handle_no_permission(self):
        return redirect('not_authorized')
    