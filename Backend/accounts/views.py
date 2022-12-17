from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from .signup_form import CreateUser
from .models import CustomUserManager

# Create your views here.


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is None:
            context = {"error": "Invalid username or password."}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect('/dashboard')
    return render(request, 'accounts/login.html', {})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})


def signup_view(request):
    form = CreateUser()
    context = {'form': form}
    form = CreateUser(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

    # form = UserCreationForm(request.POST or None)
    # if form.is_valid():
    #     user_obj = form.save()
    #     return redirect("/login")
    # context = {"form": form}
    # return render(request, "accounts/signup.html", context)
