from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from activities.models import AddActivity
from django.http import HttpResponse


# Create your views here.

@login_required
def reviews(request, activity_pk):
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
            return redirect('categories')
    
    form = ReviewForm()

    all_reviews = Review.objects.filter(activity_pk=activity)
    return render(request, 'reviews/reviews.html', {
        'form': form,
        'activity_name': activity_name,
        'reviews': all_reviews
    })

class EditReview(UserPassesTestMixin,UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/edit_reviews.html'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your review was successfully updated.')
        return redirect('categories')

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error updating your review.')
        return redirect('categories')

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to edit this review.')
        return redirect('categories')

    

