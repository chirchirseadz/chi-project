from django import forms
from .models import Message



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['your_name', 'email', 'subject', 'message']


