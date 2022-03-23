from django import forms
from .models import comment,bids

class bid_form(forms.ModelForm):
    class Meta:
        model = bids
        fields = ['bid',]

        labels = {
            'bid' : ''
        }

        widgets = {
            'bid' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Bid Here ... ',
                'rows' : 1,
                'cols' : 100,
                'step' : 0.01,
                'type' : 'number'
            })
        }

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
        

        