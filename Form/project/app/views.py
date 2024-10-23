from django.shortcuts import render
from form import UserForm
from form import ProfileForm
# Create your views here.
def home(request):
    context={}
    context['user']=UserForm
    context['profile']=ProfileForm
    return render(request,'home.html',context)