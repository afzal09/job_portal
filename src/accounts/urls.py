from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/',view=views.account_register,name="account_register"),
    path('resgiter_process/',view=views.register_process,name="register_process"),
    path('login/',view=views.account_login,name="account_login"),
    path('profile/',view=views.account_profile,name="account_profile"),
    path('logout/',view=views.account_logout,name="account_logout"),
    path('myAccount/',view=views.account_myAccount,name="account_myAccount"),
]
