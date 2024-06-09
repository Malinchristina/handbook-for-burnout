from django.contrib import admin
from .models import AddCategory

# Register your models here.

@admin.register(AddCategory)
class AddCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name', 'author', 'created_on')
    search_fields = ['category_name']
    readonly_fields = ('category_id', 'created_on')
