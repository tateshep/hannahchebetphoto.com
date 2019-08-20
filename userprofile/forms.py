from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormEmail(UserCreationForm):
    # Custom form for user creation requiring email
    
    email = forms.EmailField(required = True)
    terms_and_conditions = forms.BooleanField(widget=forms.CheckboxInput, required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2","terms_and_conditions")

    def save(self,commit=True):
        user = super(UserCreationFormEmail, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            return user


