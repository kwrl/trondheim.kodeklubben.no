from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

class UserCreateForm(UserCreationForm):
    email       = forms.EmailField(required=True)
    first_name  = forms.CharField(required=True)
    last_name   = forms.CharField(required=True)

    def __init__(self, request=None, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Brukernavn"
        self.fields['password1'].label = "Passord"
        self.fields['password2'].label = "Gjenta passord"
        self.fields['email'].label = "Epost"
        self.fields['first_name'].label = "Fornavn"
        self.fields['last_name'].label = "Etternavn"

        self.fields['username'].help_text = ""
        self.fields['password2'].help_text= ""

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name","last_name")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Brukernavn"
        self.fields['password'].label = "Passord"

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name"]
