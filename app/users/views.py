from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login_auth, logout as logout_auth
from .forms import ProfileForm, UserForm


def sign_up(request):
    """
    User signup
    """
    form_errors = []
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            for value in form.errors.values():
                form_errors.append(value)
    form = UserCreationForm()
    return render(
        request,
        'users/signup.html',
        {'form': form, 'form_errors': form_errors}
    )


def login(request):
    """
    Login user
    """
    form_errors = []
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login_auth(request, form.get_user())
            return redirect('/')
        else:
            # import ipdb; ipdb.set_trace()
            print(form.errors)
            form_errors += form.get_invalid_login_error()
    form = AuthenticationForm()
    return render(
        request,
        'users/login.html',
        {'form': form, 'form_errors': form_errors}
    )


@login_required
def logout(request):
    """
    Logout a user
    """
    logout_auth(request)
    return redirect('login')


@login_required
def profile(request):
    """
    View and update user's profile
    """
    form_errors = []
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile has been updated')

    profile_form = ProfileForm()
    user_form = UserForm(instance=request.user)

    return render(request, 'users/profile.html', {
        'profile_form': profile_form,
        'user_form': user_form,
        'form_errors': form_errors
        }
    )
