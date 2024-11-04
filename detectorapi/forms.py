from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# from phonenumber_field.phonenumber import PhoneNumber
from django.forms.widgets import TextInput
from phonenumbers import PhoneNumber




class NewsLetterForm(forms.ModelForm):
    username = forms.CharField(label='username', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = PhoneNumberField(label='phone_number', widget=PhoneNumberPrefixWidget(attrs={'placeholder': 'Phone Number'}))
    message = forms.CharField(label='message', widget=forms.Textarea(attrs={'placeholder': 'Message'}))
  
    class Meta:
        model = Contact
        fields = ['username', 'email', 'phone_number', 'message']
