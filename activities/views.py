from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AddActivityForm
from .models import AddActivity

@login_required
@user_passes_test(lambda u: u.is_staff)
def add_activity(request):
    if request.method == 'POST':
        form = AddActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.author = request.user
            activity.save()
            return redirect('activities') 
    else:
        form = AddActivityForm()
    return render(request, 'add_activity.html', {'form': form})

def activities(request):
    # Query all activities from the database
    activities_list = AddActivity.objects.all()
    return render(request, 'activities.html', {'activities': activities_list})
