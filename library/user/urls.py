from django.urls import path, include
from .views import CustomLoginView, Register
from django.contrib.auth.views import LogoutView
from . import views as user_views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),

]
