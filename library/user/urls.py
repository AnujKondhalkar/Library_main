from django.urls import path
from .views import CustomLoginView, Register
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),

]
