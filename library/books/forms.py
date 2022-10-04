from django.core import validators
from django import forms
from .models import Book


class BookRegistration(forms.ModelForm):
    # Here form is created with help of model form and required field are added in below Meta cass for model book imported from model
    # and sequence also defined.
    class Meta:
        model = Book
        fields = ['id','title','author','price','publication_date','ISBN_no']
