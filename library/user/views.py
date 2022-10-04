from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm
from django.http import HttpResponse


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
        messages.warning(
            request, f'Welcome! Please fill the form , Thank You .')
    return render(request, 'user/register.html', {'form': form})


'''
def get_name(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            obj = User.objects.get(pk=id)
            username = obj.username
            print(username)
            return HttpResponse(username)
'''
