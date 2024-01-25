from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as login_auth


def sign_up(request):
    """
    User signup
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def login(request):
    """
    Login user
    """
    if request.method == 'POST':
        import ipdb; ipdb.set_trace()
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login_auth(request, form.get_user())
            return redirect('/')
        else:
            print(form.errors)
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def profile(request):
    """
    View and update user's profile
    """
    form = {}
    return render(request, 'users/profile.html', {'form': form})
