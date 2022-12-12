from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password."}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect('/dashboard_view')
    return render(request, 'accounts/login.html', {})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})


def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login")
    context = {"form": form}
    return render(request, "accounts/signup.html", context)
