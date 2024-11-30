from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['description', 'new_request_name', 'attachment']  # Fields to show in the form
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Enter description here...'}),
            'new_request_name': forms.TextInput(attrs={'placeholder': 'Enter the name of the request...'}),
        }
