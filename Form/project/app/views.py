 
    # name=form.cleaned_data['name']
        # email=form.cleaned_data['email']
        # contact=form.cleaned_data['contact']
        # print(form )
        # data=User.objects.filter(email=email)
        # if data:
        #     msg={"Email id Allready registed"}
        #     context={}
        #     context['user']=UserForm
        #     context['profile']=ProfileForm
        #     return render (request,'home.html',{'msg':msg,'context':context} )
        # else:
        #     if form.is_valid():
        #         form.save()

from django.shortcuts import render
from .forms import UserForm,ProfileForm
from .models import User,Profile
 
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
        context={}
        context['user']=UserForm
        context['profile']=ProfileForm
        return render (request,'home.html',{'context':context} )
    else:
        context={}
        context['user']=UserForm
        context['profile']=ProfileForm
        return render (request,'home.html',{'context':context} )

def profiledata(request):
    if request.method=='POST':
        form=ProfileForm(request.POST)
        print("form")
        if form.is_valid():
            print("form is valid")
            form.save()
        context={}
        context['user']=UserForm
        context['profile']=ProfileForm
        return render (request,'home.html',{'context':context} )
    else:
        context={}
        context['user']=UserForm
        context['profile']=ProfileForm
        return render (request,'home.html',{'context':context} )

def complatedata(request):
    pro_data=Profile.objects.all()
    my_list=[]
    for i in pro_data:
        user_data=User.objects.get(name=i.pro_name)
        pro_name=i.pro_name
        quali=i.quali
        city=i.city
        email=user_data.email
        contact=user_data.contact
        data={
            'name':pro_name,
            'quali':quali,
            'city':city,
            'email':email,
            'contact':contact
        }
        my_list.append(data)
        print(my_list)
    return render(request,'complatedata.html',{'my_list':my_list})