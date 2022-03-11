from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from CriptoTracking.forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

def home(request):
    return render(request, "home.html")