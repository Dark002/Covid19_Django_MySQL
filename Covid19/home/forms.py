from django import forms
from crispy_forms.helper import FormHelper

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')