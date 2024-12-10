from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Profile


#Create User (Model Form)
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    role = forms.ChoiceField(
        choices=[('', 'Select Role')] + Profile.ROLE_CHOICES,
        required=True,
        help_text="Select your role in the system"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')

        # Check if a user with the same username and first name exists
        if User.objects.filter(username=username, first_name=first_name).exists():
            raise forms.ValidationError(
                "A user with this username and first name already exists. Please choose a different combination."
            )

        return cleaned_data

# Authenicate a user (Model Form)
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={'autocomplete': 'username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'})
    )