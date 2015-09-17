from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class SignupForm(UserCreationForm):
    username = forms.CharField(required=True,max_length=30,validators=[RegexValidator('^[A-Za-z0-9]{1,30}$','e.g. must be 30 characters or less','Invalid Entry')])
    email = forms.EmailField(required=True, max_length=75)
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ("username", "email", "password1","password2")

	def save(self, commit=True):
	    user = super(SignupForm, self).save(commit=False)
	    user.username = self.cleaned_data["username"]
	    user.email = self.cleaned_data["email"]
	    user.password = self.cleaned_data["password1"]
	    if commit:
	        user.save()
	    return user