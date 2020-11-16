from django import forms
from crispy_forms.helper import FormHelper

class world_form(forms.Form):
    country=forms.CharField(label='Country', max_length=255)
    date=forms.DateField(label='Date')
