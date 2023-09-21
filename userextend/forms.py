from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from userextend.models import UserProfile


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter username'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter last name'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter first name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter email'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please reenter password'})


class UserProfileForm(forms.ModelForm):
    phone = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    birth_date = forms.DateField()

    class Meta:
        model = UserProfile
        fields = ['phone', 'city', 'country', 'birth_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter phone number'})
        self.fields['city'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter city'})
        self.fields['country'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter country'})
        self.fields['birth_date'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter password'})
