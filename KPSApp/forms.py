# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32,
        error_messages={
            'required': 'Моля въведете потребителско име.',
            'max_length': 'Дължината на потребителското име е прекалено голяма.'
        }
    )
    password = forms.CharField(widget=forms.PasswordInput(), max_length=32,
        error_messages={
            'required': 'Моля въведете парола.',
            'max_length': 'Дължината на паролата е прекалено голяма.'
        }
    )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

class CheckForm(forms.Form):
    rooms_field = forms.CharField(label='Въведете стаи, отделени от запетая:', widget=forms.Textarea(attrs={'rows':3}))