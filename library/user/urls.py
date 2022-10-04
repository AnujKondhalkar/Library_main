from django.urls import path, include
from .views import register
from django.contrib.auth.views import LogoutView
from . import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', user_views.register, name='register'),
    #path('get_name/', user_views.get_name, name='get_name'),
]
