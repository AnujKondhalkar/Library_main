from django.urls import path, include
# include is used to bring path (routes) from urls file of other apps

from .views import register # register form is imported to in respective template
from django.contrib.auth.views import LogoutView # predefined view for logout the user.
from . import views as user_views # views are imported ---> in such a way that all models , views, templates are combined to show business logic .
from django.contrib.auth import views as auth_views

# This list will have the paths of every views which will be able to show business logic in templates
urlpatterns = [
    path('register/', user_views.register, name='register'),
    # pre_define login and logout views from django library
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', user_views.register, name='register'),
    # path('get_name/', user_views.get_name, name='get_name'),
]
