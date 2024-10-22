from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.data, name='data'),
    # path('userdata/', views.userdata, name='userdata'),
]