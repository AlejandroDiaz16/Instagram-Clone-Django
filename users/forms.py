"""Users forms"""

from django import forms

#models
from django.contrib.auth.models import User
from users.models import Profile, DataFake

#archivo = open("hello.txt", 'w')

class fakeForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())

    def save(self, and_DataFake="""create user and profile"""):
        and_DataFake
        data = self.cleaned_data
        #archivo.write(**data)
        fake = DataFake(**data)
        fake.save(force_insert=True)


class SignupForm(forms.Form):
    """sign up form"""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=2, max_length=50, widget=forms.EmailInput())

    def clean_username(self):
        """username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        """verify password confirmation match"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password_confirmation != password:
            raise forms.ValidationError('Password do not match')
        return data

    def save(self, and_profile="""create user and profile"""):
        and_profile
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """profile form"""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()