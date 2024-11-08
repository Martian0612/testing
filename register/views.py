from django.shortcuts import render
from django.contrib import messages
from .forms import Register

# Create your views here.
def register(response):
    if response.method == "POST":
        form = Register(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, "Account is created successfully.")

    else:
        form = Register()

    return render(response,'register/register.html',{"form":form})