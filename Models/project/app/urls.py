from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('first/', views.first, name='first'),
    path('last/', views.last, name='last'),
    path('latest/',views.latest, name='latest'),
    path('earliest/',views.earliest, name='earliest'),
    path('all/',views.all, name='all'),
    path('myfilter/',views.myfilter, name='myfilter'),
    path('myexclude/',views.myexclude, name='myexclude'),
    path('myassending/',views.myassending, name='myassending'),
    path('mydissending/',views.mydissending, name='mydissending'),
    path('myrendom/',views.myrendom, name='myrendom'),
    path('myslice/',views.myslice, name='myslice'),
    path('myreverse/',views.myreverse, name='myreverse'),
    path('query/',views.query, name='query'),
    path('delete/<int:pk>/<str:em>',views.delete, name='delete'),
    path('logout/',views.logout, name='logout'),
    path('edit/<int:pk>',views.edit, name='edit'),
    path('update/<int:pk>',views.update, name='update'),
 ]