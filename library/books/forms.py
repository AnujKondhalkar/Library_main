from django.core import validators
from django import forms
from .models import Book


class BookRegistration(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['id','title','author','price','publication_date','ISBN_no']
