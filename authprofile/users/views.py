from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm


def signup (request):
    if request.method=="POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get(username)
            messages.success(request, f'Account Created for {username} !')
            return redirect("#")
    else:
        form = UserSignupForm()
    return render(request, "registration/signup.html", {'form':form})
