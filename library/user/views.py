from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hello {username} Your account has been created! You are now able to log in.')
            return redirect('login')
    else:                                              # Else for 'GET' request
        form = UserRegisterForm()
        messages.info(
            request, f'Welcome! Please fill the form , Thank You .')
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # u_form and p_form these forms are rendered from users/forms.py
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(
                request.POST,
                instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(
                    request, f'Your account has been updated!')
                return redirect('profile')

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
    else:                   # if not request.user.is_authenticated
        messages.info(
            request, f'You need to log in first! to access this page.')
        return redirect('login')

    return render(request, 'users/profile.html', context)
