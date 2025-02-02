from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  


class UserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['name', 'email', 'phone', 'course']
        labels = {
            "name": "Student name",
            "email": "Email",
            "phone": "Phone No",
            "course": "Choose a course"
        }

class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(
        required=False,  # Optional field
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter a new password'}),
        help_text="Leave blank to keep the current password."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:  # Update only if a password is entered
            user.set_password(password)
        if commit:
            user.save()
        return user