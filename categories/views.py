from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AddCategory
from .forms import CategoryForm

# Create your views here.

# View to list categories
def category_list(request):
    categories = AddCategory.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})
    
# View to add a new category (with authentication check)
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

# Views for the categories
def routines_view(request):
    return render(request, 'categories/routines.html')


def podcasts_view(request):
    return render(request, 'categories/podcasts.html')


def indoor_activities_view(request):
    return render(request, 'categories/indoor_activities.html')


def outdoor_activities_view(request):
    return render(request, 'categories/outdoor_activities.html')