from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def activities(request):
    return render(request, 'activities.html')
