from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(label='Enter your review here:',
    widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))

    class Meta:
        model = Review
        fields = ['comment']
