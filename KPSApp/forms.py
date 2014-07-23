# -*- coding: utf-8 -*-
from django import forms

class CheckForm(forms.Form):
    rooms_field = forms.CharField(label='Въведете стаи, отделени от запетая:', widget=forms.Textarea(attrs={'rows':3}))