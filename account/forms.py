from django import forms
from django.contrib.auth.forms import UserCreationForm

ACCOUNT_TYPE_CHOICES = [
    ('Parent', 'Parent'),
    ('Personal', 'Personal'),

    ]

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "name": "email",
            "id": "email",
        }))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "name": "password",
            "id": "password",
        }))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "name": "confirmPassword",
            "id": "confirmPassword",
        }))


class LearnerSignupForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "name": "firstName",
            "id": "firstName",
        }))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "name": "lastName",
            "id": "lastName",
        }))

    middle_initial = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "name": "middleInitial",
            "id": "middleInitial",
        }))



    date_of_birth = forms.CharField(widget=forms.DateInput(
        attrs={
            "class": "form-control",
            "name": "dob",
            "id": "dob",
        }))





    account_type = forms.CharField(
        label='What is your favorite fruit?',
        widget=forms.RadioSelect(
            attrs = {
                "name": "accountType",
            },
            choices = ACCOUNT_TYPE_CHOICES
        ))


class TutorSignupForm(UserCreationForm):
    pass


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
