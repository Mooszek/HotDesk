from django import forms
from datetime import date
from .models import Room

class SearchRoomForm(forms.Form):
    room = forms.ModelChoiceField(required=True, queryset=Room.objects.all())
    
    start_date = forms.DateField(required=True, initial=date.today(),
        widget=forms.TextInput(
            attrs={'type': 'date', 'min': date.today() }) 
    )   
    end_date = forms.DateField(required=True, initial=date.today(),
        widget=forms.TextInput(
            attrs={'type': 'date', 'min': date.today() } ) 
    )   