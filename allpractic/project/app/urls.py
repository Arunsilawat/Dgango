from django.urls import path,include
from app import views
urlpatterns = [
     path("firstRender/",views.firstRender,name="firstRender"),
     path("firstHttpResponse/",views.firstHttpResponse,name="firstHttpResponse"),
     path("firstredirect/",views.firstredirect,name="firstredirect"),
     path("firstJsonResponse/",views.firstJsonResponse,name="firstJsonResponse")
]