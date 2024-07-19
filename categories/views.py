from django.shortcuts import render
from django.http import HttpResponse
from . import views
from django.urls import path
from .models import AddCategory
from .forms import CategoryForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def categories(request):
    return HttpResponse('This is the categories app')

@login_required
def add_category(request):
    if not request.user.is_staff:
        return HttpResponse('Unauthorized', status=401)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.author = request.user  # Automatically set the author to the current user
            category.save()
            return HttpResponse('Category added')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})
