from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,JsonResponse

def firstRender(request):
    return render(request,"home.html")

def firstHttpResponse(request):
    return HttpResponse("<h1>Arun </h1>")

def firstredirect(request):
    return redirect("https://www.google.com")

def firstJsonResponse(request):
    data={"name":"Arun","age":23}
    return JsonResponse(data)