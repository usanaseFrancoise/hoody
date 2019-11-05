from .models import *
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']


class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name','location','occupants']

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','user_name','bio')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','bio']
