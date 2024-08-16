from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AddCategory
from .forms import CategoryForm

# Create your views here.


def category_list(request):
    categories = AddCategory.objects.all()
    return render(request, 'categories/categories.html', {
                  'categories': categories})


# Below view is there for future US to add a new category outside admin panel

# View to add a new category (with authentication check)
@login_required
def add_category(request):
    if not request.user.is_staff:
        return HttpResponse('Unauthorized', status=401)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.author = request.user
            category.save()
            return HttpResponse('Category added')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})
