from django import forms

from ecomapp.models import ContactMessage


class MessageContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={"type": "text", "name": "customerName", "id": "customername", 'class': 'input', 'placeholder': 'Input Your Name ..'}),
            'subject': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Input Your Subjects ..'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Input Your Email ..'}),
            'message': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Input Your Message ..'}),
        }

class SearchForms(forms.Form):
    query = forms.CharField(max_length=300)
    cat_id = forms.IntegerField()