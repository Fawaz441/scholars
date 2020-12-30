from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

from .forms import SignupForm,LoginForm
from .models import Profile

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            phone_number = form.cleaned_data.get("phone_number")
            password = form.cleaned_data.get("password")

            user = User.objects.create(
                username = username,
                email = email,
            )
            user.set_password(password)
            user.save()
            profile = Profile.objects.create(user=user,phone_number=phone_number)
            profile.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    return render(request,'users/signup.html',{'form':form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("users:dashboard")
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    return redirect('users:dashboard')
        else:
            form = LoginForm()
        return render(request,'users/login.html',{'form':form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('scholars:homepage')

def dashboard(request):
    return render(request,'users/dashboard.html')
    





