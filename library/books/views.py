from django.shortcuts import render

# Create your views here.


def show(request):
    return render(request, 'books/show.html')


def add(request):
    return render(request, 'books/add.html')
