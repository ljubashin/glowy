from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm, UpdateProfileForm, ImageUpdateForm
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Oh no! Something went wrong, but you can always try again!"))
            return redirect('login')

    return render(request, 'logiranje/login.html',{})

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'logiranje/register_user.html', {
        'form': form,
    })

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def profil(request):
    if request.method == 'POST':
        username_form = UpdateProfileForm(request.POST, instance=request.user)
        img_form = ImageUpdateForm(request.POST, request.FILES, instance=request.user.profil)
        if username_form.is_valid() and img_form.is_valid():
            username_form.save()
            img_form.save()
            messages.success(request, ("User information is successfully saved!"))
            return redirect('profile')
    else:
        username_form = UpdateProfileForm(instance=request.user)
        img_form = ImageUpdateForm(instance=request.user.profil)

    context = {
        "username_form": username_form,
        "img_form": img_form
    }
    return render(request, 'logiranje/profil.html',context)