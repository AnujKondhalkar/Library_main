from django.db import models

# Create your models here.


# title, author,price, publication_date, ISBN_no

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
    publication_date = models.CharField(max_length=200)
    ISBN_no = models.IntegerField(blank=True, null=True)
