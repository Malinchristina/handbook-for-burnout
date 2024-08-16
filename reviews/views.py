from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from activities.models import AddActivity
from django.http import HttpResponse, HttpResponseForbidden



# Create your views here.

@login_required
def add_review(request, activity_pk):
    activity = get_object_or_404(AddActivity.objects.filter(pk=activity_pk))
    activity_name = activity.activity_name

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            author = request.user

            review = Review.objects.create(
                comment=comment,
                activity_pk=activity,
                author=author
            )

            review.save()
            messages.success(request, 'Your review was successfully added.')
            return redirect('activity_reviews', pk=activity_pk)

    form = ReviewForm()

    all_reviews = Review.objects.filter(activity_pk=activity)
    return render(request, 'reviews/add_review.html', {
        'form': form,
        'activity_name': activity_name,
        'reviews': all_reviews
    })


class ReviewsView(ListView):
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

    def post(self, request, *args, **kwargs):
        activity_pk = request.POST.get('activity_pk')
        activity = get_object_or_404(AddActivity, pk=activity_pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.activity_pk = activity
            review.author = request.user
            review.save()
            return redirect('activity_reviews', pk=activity.pk)
        else:
            return self.get(request, *args, **kwargs)


def not_authorized(request):
    return render(request, '403.html')


class EditReview(UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/edit_reviews.html'

    def get_success_url(self):
        return reverse_lazy('activity_reviews', kwargs={'pk': self.object.activity_pk.pk})

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your review was successfully updated.')
        return redirect('activity_reviews', pk=activity_pk.pk)

    def form_invalid(self, form):
        messages.error(self.request,
                       'There was an error updating your review.')
        return redirect('categories')

    def handle_no_permission(self):
        return not_authorized(self.request)


class DeleteReview(UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/delete_review.html'

    def get_success_url(self):
        return reverse_lazy('activity_reviews', kwargs={'pk': self.object.activity_pk.pk})

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your review was successfully deleted.')
        return super().delete(request, *args, **kwargs)

    def handle_no_permission(self):
        return not_authorized(self.request)


