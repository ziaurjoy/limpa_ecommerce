

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from user_app.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'Write Your Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": 'Write Your Email'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'Write Your First Name'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re Password'})
        }



class UserUpdate(UserChangeForm):
    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Enter Your Email'})
        }


city = [
    ('Dhaka', 'Dhaka'),
    ('Mymensign', 'Mymensign'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Barisal', 'Barisal'),
    ('Chottogram', 'Chottogram'),
    ('Khulna', 'Khulna'),
]


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'phone', 'address', 'country', 'city', 'image']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Full Name'}),
            'phone': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Address'}),
            'country': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Country'}),
            'city': forms.Select(attrs={'class': 'input', 'placeholder': 'City', }, choices=city),
            'image': forms.FileInput(attrs={'class': 'input', 'placeholder': 'Image'}),
        }

