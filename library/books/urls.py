from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('add_book/', views.add_book, name="add_book"),
    path('show_book/', views.show_book, name="show_book"),
    path('update_book/', views.update_book, name="update_book"),
    path('delete_book/<int:id>/', views.delete_book, name="delete_book"),
    path('edit_book/<int:id>/', views.edit_book, name="edit_book"),
]
