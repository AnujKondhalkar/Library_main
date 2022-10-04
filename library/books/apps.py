from django.apps import AppConfig

# app Book is configured here which will be added in INSTALLED_APPS in settings.py

class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'
