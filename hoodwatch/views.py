from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hoodwatch.models import Post,Profile,Neighbourhood,Business,Join
from django.http import HttpResponse
from .models import Post,Profile,Neighbourhood,Business,Join
from django.contrib import messages
from . forms import NewPostForm,UserForm,CreateHoodForm,ProfileForm
from django.contrib.auth.models import User

# Create your views here.
