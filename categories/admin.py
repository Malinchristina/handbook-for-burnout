from django.contrib import admin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from .models import AddCategory

# Register your models here.

@admin.register(AddCategory)
class AddCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name', 'author', 'created_on')
    search_fields = ['category_name']
    readonly_fields = ('category_id', 'created_on')

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
            # If the save is successful, only display success message
            self.message_user(request, f'The category "{obj.category_name}" was added/updated successfully.', level='SUCCESS')
        except ValidationError as e:
            # If there's a validation error, only display error message
            self.message_user(request, str(e), level='ERROR')

    def response_add(self, request, obj, post_url_continue=None):
        # Override the response after adding a new category
        if '_continue' not in request.POST:
            # Redirect to the category list page if not continuing
            return HttpResponseRedirect('/admin/app_name/addcategory/')
        else:
            # Continue editing the category if requested
            return super().response_add(request, obj, post_url_continue)