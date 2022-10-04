from django.db import models

# Create your models here.

# Attributes ----> title, author,price, publication_date, ISBN_no
"""
Here the model is created for the Book in such a way that the Object Book will have attributes mentioned above with
their perticular requied data field with respective data content with contraints
this will be used to create database model to store the data in DATABASE (sql, mysql etc...)
ORM functionality will be use to map those data and fields with respective different types of DBMS. SqLite is inbuilt and predifined DB for Django.
"""

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
    publication_date = models.CharField(max_length=200)
    ISBN_no = models.CharField(max_length=20)
