from django.contrib import admin
from .models import Book

# Register your models here.

# This book model is registered to database which can be accessed
# via admin panel by superuser which have all permision to do operation on it.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author','price', 'publication_date', 'ISBN_no')
