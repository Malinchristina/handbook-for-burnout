from django import forms
from .models import AddActivity


class AddActivityForm(forms.ModelForm):
    class Meta:
        model = AddActivity
        fields = ['activity_name', 'description', 'category', 'url_link',
                  'level']