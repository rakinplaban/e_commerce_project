from django import forms
from .models import comment

class comment_form(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['content',]
        
        widgets = {
            'content' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Add Comment ...',
                'rows' : 1,
                'cols' : 100
            })  
        }
        labels = {
            'content' : ''
        }
        

        