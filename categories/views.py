from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testing_categories(request):
    return HttpResponse('This is the categories app')
