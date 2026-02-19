from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import MyCustomRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



def register_view(request):
    if request.method == 'POST':
        form = MyCustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('profile')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = MyCustomRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        email = request.POST.get('email')
        user.email = email
        user.save()
    return render(request, 'blog/profile.html', {'user': user})
