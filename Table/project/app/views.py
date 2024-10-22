from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
# def userdata(request):
#     if request.method=='POST':
#         fname=request.POST.get("fname")
#         lname=request.POST.get("lname")
#         email=request.POST.get("email")
#         carnm=request.POST.get("carnm")
#         amount=request.POST.get("cpay")
#         address=request.POST.get("add")
#         pick=request.POST.get("pick")
#         drop=request.POST.get("drop")
#         feed=request.POST.get("feed")
#         Bookingdata.objects.create(fname=fname,lnam=lnamee,email=email,carnm=carnm,amount=amount,address=address,pick=pick,drop=drop,feedback=feed)
#         return render(request,'home.html')
def data(request):
    if request.method=='POST':
        name=request.POST.get('nm')
        age=request.POST.get('age')
        contact=request.POST.get('con')
        User.objects.create(name=name,age=age,contact=contact)
        return render(request,'home.html')