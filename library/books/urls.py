from . import views
from django.urls import path


urlpatterns = [
    # index page named home as defined
    path('', views.home, name="home"),
    # this view will be used by admin only to Add a book to db --- Create
    path('add_book/', views.add_book, name="add_book"),
    # this view will be used by Every Authenticated user to See all book list from db ---- Retrieve
    path('show_book/', views.show_book, name="show_book"),
    # this view will be used by admin only to Edit data of existing book in db --- Update
    path('update_book/', views.update_book, name="update_book"),
    path('edit_book/<int:id>/', views.edit_book, name="edit_book"),
    # this view will be used by admin only to Remove data of existing book to db --- Delete
    path('delete_book/<int:id>/', views.delete_book, name="delete_book"),

    # e.g. this "add_book" in name="add_book" is used to get url in HTML as {% url 'add_book' %} id for object {% url 'add_book' id %}
]
