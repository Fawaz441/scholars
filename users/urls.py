from django.urls import path
from .views import signup,login_view,logout_view,dashboard
from main.views import admin_view

app_name = 'users'
urlpatterns = [
    path('signup',signup,name='signup'),
    path('login',login_view,name='login'),
    path('logout',logout_view,name='logout'),
    path('dashboard',dashboard,name='dashboard'),
    path('boss2',admin_view,name = 'boss2'),
]