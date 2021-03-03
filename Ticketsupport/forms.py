from django import forms
from .models import catagory

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', required = True, max_length=100)
    email = forms.EmailField(required=True)
    catagory = forms.ChoiceField(choices = catagory,) #choices in models.py
    comments = forms.CharField(max_length=300, widget=forms.Textarea, required=True,)
