from django.contrib import admin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from .models import Review

# Register your models here.


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ('activity_pk', 'author', 'comment', 'created_on')
    search_fields = ['activity_pk']
    readonly_fields = ('activity_pk', 'created_on')
