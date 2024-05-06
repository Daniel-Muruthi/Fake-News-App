from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# from phonenumber_field.phonenumber import PhoneNumber
from django.forms.widgets import TextInput
from phonenumbers import PhoneNumber



class CustomPhoneNumberPrefixWidget(PhoneNumberPrefixWidget):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs.update({'style': 'width: 100%; display: inline-block;'})  # Adjust styling if needed

    def subwidgets(self, name, value, attrs=None):
        number = PhoneNumber.from_string(value or '', 'US')  # Use 'US' for default country
        prefix_widget = super().subwidgets(number.as_international(), name, attrs)[0]  # Get country code with flag
        return [prefix_widget, TextInput(attrs={'style': 'width: 75%;'})]  # Return both country code and input field


class NewsLetterForm(forms.ModelForm):
    username = forms.CharField(label='username', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username', 'style':'color: #fff'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = PhoneNumberField(label='phone_number', widget=CustomPhoneNumberPrefixWidget(attrs={'class': 'input','placeholder': 'Phone Number'}))
    message = forms.CharField(label='message', widget=forms.Textarea(attrs={'placeholder': 'Message'}))
  
    class Meta:
        model = Contact
        fields = ['username', 'email', 'phone_number', 'message']
