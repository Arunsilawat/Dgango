from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path('',views.home, name='home'),
    path('collection/',views.collection, name='collection'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'), 
    path('registerdata/',views.registerdata, name='registerdata'), 
    path('logout/',views.logout, name='logout'), 
]
