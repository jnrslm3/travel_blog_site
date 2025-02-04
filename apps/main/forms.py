from django import forms
from .models import ContactUs, Subscription


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'text']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Subject"}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Text"}),
        }

class SubscriptionForm(forms.ModelForm):
    model = Subscription
    fields = 'email'
    widgets = {
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
    }

