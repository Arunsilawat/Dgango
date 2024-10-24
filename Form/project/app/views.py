# from django.shortcuts import render
# from .forms import UserForm
# from .forms import ProfileForm
# # Create your views here.
# def home(request):
#     context={}
#     context['user']=UserForm
#     context['profile']=ProfileForm
    
#     return render(request,'home.html',context)


from django.shortcuts import render
from .forms import UserForm,ProfileForm
from .models import User
# Create your views here.

def home(request):
    context={}
    context['user']=UserForm
    context['profile']=ProfileForm

    return render (request,'home.html',{'context':context} )

def userdata(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        contact=form.cleaned_data['contact']
        # print(form )
        data=User.objects.filter(email=email)
        if data:
            msg={"Email id Allready registed"}
            context={}
            context['user']=UserForm
            context['profile']=ProfileForm
            return render (request,'home.html',{'msg':msg,'context':context} )
        else:
            if form.is_valid():
                form.save()
    else:
        context={}
        context['user']=UserForm
        context['profile']=ProfileForm
        return render (request,'home.html',{'context':context} )

def profiledata(request):
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        context={}
        context['user']=UserForm
        context['profile']=ProfileForm
        return render (request,'home.html',{'context':context} )