from django.shortcuts import render

# Create your views here.
def home(request):
    # data1={'name':'Arun','age':24,'city':'Bhopal'}
    # data2={'name':'Rahul','age':20,'city':'Betul'}
    # data3={'name':'Sonam','age':21,'city':'Jabalpur'}
    # data4={'name':'Mukesh','age':29,'city':'Jaipur'}
    data1={'name':'Mukesh','age':29,'city':'Jaipur'}
    data2={}
    data3={}
    data4={}
    return render(request,'index.html',{'key1':data1,'key2':data2,'key3':data3,'key4':data4})
