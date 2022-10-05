from django.shortcuts import render, redirect, HttpResponseRedirect
# After all views successfull a view function being called then render , redirect and
# HttpResponseRedirect will help user to get requested web page.
from .forms import BookRegistration
# book instance by BookRegistration
from .models import Book
# Just To Retrieve A book object
from django.contrib import messages
# Interactive Information message
from django.contrib.auth.models import User


# def base(request, id):
#     if user.is_authenticated:
#         obj = User.objects.get(pk=id)
#         username = obj.username
#         print(username)
#     else:
#         username = "Hello Guest!"
#     return render(request, 'books/base.html', {'username': username})


def get_username(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'Guest'
    return username


# Book_title = []


def home(request):
    username = get_username(request)
    return render(request, 'books/home.html', {'username': username})


# title, author,price, publication_date, ISBN_no

# All are function based views show below
# CREATE
def add_book(request):
    if request.user.is_superuser:   # this Perticula view can only be accessed by Admin a.k.a superuser
        if request.method == 'POST':  # Post Request when url is hit while submision of form
            # Registration form is created with BookRegisterForm Class
            form_ = BookRegistration(request.POST)

            # is_valid() function will chake that the content in every input box is suitable for that box
            # e.g. email box must contain @ symbol between two word and at the end .com or .in like domain must be there.
            if form_.is_valid():
                '''
                tl, au, pr, pd, isbn, b_data have reference of cleaned data of Book object
                which will be used to save those in DATABASE.
                form_.cleaned_data['title'], cleaned_data is the dictionary of validated data in form input box.
                e.g title is the key of input data which will be considered as value.
                '''
                tl = form_.cleaned_data['title']
                au = form_.cleaned_data['author']
                pr = form_.cleaned_data['price']
                pd = form_.cleaned_data['publication_date']
                isbn = form_.cleaned_data['ISBN_no']
                b_data = Book(title=tl, author=au, price=pr,
                              publication_date=pd, ISBN_no=isbn)
                b_data.save()  # saved in DB

                '''
                Book_title.append(tl)
                ##########

                if len(Book_title) == 0:
                    return None
                else:
                    print(Book_title)
                '''
                messages.success(
                    request, f'{tl} is successfully added!')
                return redirect('show_book')

        else:             # Else for 'GET' request at the initial stage when url is being hit.

            form_ = BookRegistration()
        return render(request, 'books/add.html', {'form': form_})
    else:
        # It will Show message the at the web page body where ever you use message tag it will replace that varible tag and display message.
        # render function will take the context data like form dictionary , message , and bring that all to the provided template which is rendered from it's location
        # "warning" in messages.warning is css design
        # success,warning,danger, primery etc. are meessage css design variable
        messages.warning(
            request, "Only Admin Have Permission To Add A Book!")
        return redirect('home')  # Only admin can use this view

# RETRIEVE


def show_book(request):
    if request.user.is_authenticated:
        book_list = Book.objects.all()
        # All book objects are retrieved and mentioned in context data dictionary {'book_data': book_list}
        # which will be rendered and every element in that context data will be shown in html page
        return render(request, 'books/show.html', {'book_data': book_list})
    else:
        messages.info(      # Only authenticated user can use this view
            request, f"You Need To LogIn to Access Show Book Page")
        return redirect('login')


# UPDATE


def update_book(request):
    if request.user.is_superuser:  # Admin required to use this view
        # All book objects are retrieved and mentioned in context data dictionary {'book_data': book_list}
        book_list = Book.objects.all()

        return render(request, 'books/update.html', {'book_data': book_list})
    else:
        messages.warning(
            request, "Only Admin Have Permission To Update A Book!")
        # It will Show message the at the web page body where ever you use message tag it will replace that varible tag and display message.
        # render function will take the context data like form dictionary , message , and bring that all to the provided template which is rendered from it's location
        # "warning" in messages.warning is css design
        return redirect('home')  # Only admin can use this view


def edit_book(request, id):  # view for edit data of an object here e.g. book object
    if request.user.is_superuser:  # Admin required to use this view
        if request.method == 'POST':  # Admin will get data from db
            # id is used to find the data id of object will be get by that view which will be helpful to access that data from DB.
            obj = Book.objects.get(pk=id)
            # form object will be created with data already inserted via POST request
            form_ = BookRegistration(request.POST, instance=obj)
            if form_.is_valid():  # data will be validated
                # get the element of an object dictionary here e.g. 'title'
                tl = form_.cleaned_data['title']
                form_.save()  # save that data to database
                messages.warning(  # already explained above about message
                    request, f'Data of {tl} is successfully updated!')
                # after operaion bring user to update_book page
                return redirect('update_book')
        else:
            obj = Book.objects.get(pk=id)  # id is used to get Book object
            # fill data data of form by object accessed via id
            form_ = BookRegistration(instance=obj)
        # after successful validation this respective html document will be rendered with form filled already
        return render(request, 'books/edit_book.html', {'form': form_})
    else:
        messages.warning(
            request, "Only Admin Have Permission To Update A Book!")  # if not admin bring user to home page
        return redirect('home')

# DELETE


def delete_book(request, id):  # view for delete an object here e.g. book object
    if request.user.is_superuser:  # Admin required to use this view
        if request.method == "POST":  # Admin will get data from db
            # id is used to find the data id of object will be get by that view which will be helpful to access that data from DB.
            obj = Book.objects.get(pk=id)
            print(obj.title)  # title of that book object
            # built in delete function of object book object class will be used to delete that respective book object.
            obj.delete()
            # message explained bove multiple times
            messages.info(
                request, f'Book {obj.title} is successfully deleted!')
            return redirect('update_book')
    else:
        messages.warning(
            request, "Only Admin Have Permission To Delete A Book!")  # if not admin this message will be printed
        return redirect('home')
