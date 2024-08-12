from django.contrib import admin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from .models import AddActivity

# Register your models here.


@admin.register(AddActivity)
class AddActivity(admin.ModelAdmin):
    list_display = ('activity_id', 'activity_name', 'category', 'author',
                    'created_on')
    search_fields = ['activity_name']
    readonly_fields = ('activity_id', 'created_on')
