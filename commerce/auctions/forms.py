from django import forms
from .models import comment

class comment_form(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['content',]

        