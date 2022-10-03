from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import BookRegistration
from .models import Book
from django.contrib import messages

# Create your views here.

Book_title = []


def home(request):
    return render(request, 'books/home.html')


# title, author,price, publication_date, ISBN_no


def add_book(request):
    if request.method == 'POST':
        form_ = BookRegistration(request.POST)
        if form_.is_valid():
            tl = form_.cleaned_data['title']
            au = form_.cleaned_data['author']
            pr = form_.cleaned_data['price']
            pd = form_.cleaned_data['publication_date']
            isbn = form_.cleaned_data['ISBN_no']
            b_data = Book(title=tl, author=au, price=pr,
                          publication_date=pd, ISBN_no=isbn)
            b_data.save()
            Book_title.append(tl)
            ##########

            if len(Book_title) == 0:
                return None
            else:
                print(Book_title)
            messages.warning(
                request, f'{tl} is successfully added!')
            return redirect('show_book')

    else:
        form_ = BookRegistration()
    return render(request, 'books/add.html', {'form': form_})


def show_book(request):
    book_list = Book.objects.all()
    return render(request, 'books/show.html', {'book_data': book_list})


def update_book(request):
    book_list = Book.objects.all()
    return render(request, 'books/update.html', {'book_data': book_list})


def delete_book(request, id):
    if request.method == "POST":
        obj = Book.objects.get(pk=id)
        print(obj.title)
        obj.delete()
        messages.info(
            request, f'Book {obj.title} is successfully deleted!')
        return redirect('update_book')


def edit_book(request, id):
    if request.method == 'POST':
        obj = Book.objects.get(pk=id)
        form_ = BookRegistration(request.POST, instance=obj)
        if form_.is_valid():
            tl = form_.cleaned_data['title']
            form_.save()
            messages.warning(
                request, f'Data of {tl} is successfully updated!')
            return redirect('show_book')
    else:
        obj = Book.objects.get(pk=id)
        form_ = BookRegistration(instance=obj)
    return render(request, 'books/edit_book.html', {'form': form_})
