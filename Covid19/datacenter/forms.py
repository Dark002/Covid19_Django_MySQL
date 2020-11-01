from django import forms

class world_form(forms.Form):
    country=forms.CharField(label='country', max_length=255)
    date=forms.DateField(label='date')
class statewise_form(forms.Form):
    state_name=forms.CharField(label='state_name', max_length=255)