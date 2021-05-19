# /register - display the string "placeholder for users to create a new user record"
# /login - display the string "placeholder for users to log in"
# /users/new - have the same method that handles /register also handle the url request of /users/new
# /users - display the string "placeholder to later display all the list of users"

from django.urls import path 
from . import views

urlpatterns = [
    path('register',views.register),
    path('login',views.login),
    path('users/new',views.new),
    path('users',views.users),

]