from django import forms
from .models import AddCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = AddCategory
        fields = ['category_name']
