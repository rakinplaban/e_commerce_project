from django import forms
from .models import auction_listing

class auction_listing_form(forms.ModelForm):
    class Meta:
        model = auction_listing
        fields = ('title','description','starting_bid','category','img',)