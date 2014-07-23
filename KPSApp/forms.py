from django import forms

class CheckForm(forms.Form):
    rooms_field = forms.CharField(label='Rooms')