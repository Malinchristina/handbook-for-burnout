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
