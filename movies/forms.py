from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    """Form fo Reviews"""
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'text']

