from django.shortcuts import render, redirect
from django.contrib import messages
# imported the message function for interactive response on webpage of app
# imported from from via . (local) directory for creation of form instance of UserRegisterForm
from . forms import UserRegisterForm
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':  # Post Request when url is hit while submision of form
        # Registration form is created with UserRegisterForm Class
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            # is_valid() function will chake that the content in every input box is suitable for that box
            # e.g. email box must contain @ symbol between two word and at the end .com or .in like domain must be there.

            form.save()  # After succesful validation the data in the form will be saved in database
            # access username for specific purpose like use in message body
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hello {username} Your account has been created! You are now able to log in.')
            return redirect('login')
    # Else for 'GET' request at the initial stage when url is being hit.
    else:
        form = UserRegisterForm()  # it will bring an empty form for user.
        messages.warning(
            request, f'Welcome! Please fill the form , Thank You .')  # It will Show message the at the web page body where ever you use message tag it will replace that varible tag and display message.
        # render function will take the context data like form dictionary , message , and bring that all to the provided template which is rendered from it's location
        # "warning" in messages.warning is css design
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
