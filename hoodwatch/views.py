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
def index(request):
    hoods = Neighbourhood.objects.all()
    business = Business.objects.all()
    posts = Post.objects.all()
    print(posts)
    return render(request, 'index.html',locals())



@login_required(login_url='/accounts/login/')
def profile(request,user_id=None):
    if user_id == None:
        user_id=request.user.id
    current_user = User.objects.get(id = user_id)
    user = current_user
    images = Post.objects.filter(user=current_user)
    profile = Profile.objects.all()
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login')
def updateprofile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
			form = ProfileForm()
	return render(request, 'updateprofile.html',{"form":form })



@login_required(login_url='/accounts/login/')
def createHood(request):
    if request.method == 'POST':
        form = CreateHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit = False)
            hood.user = request.user
            hood.save()
       
        return redirect('index')
    else:
        form = CreateHoodForm()
        return render(request,'new_hood.html',{"form":form})


def search(request):

    if request.GET['hoods']:
        search_term = request.GET.get("hoods")
        hoods = Neighbourhood.search_hood(search_term)
        message = f"{search_term}"

        return render(request,'search.html',locals())

    else:
        message = "You Haven't searched for any item"
        return render(request,'search.html',locals())



@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('hoods')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})
