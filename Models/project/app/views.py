from django.shortcuts import render
from.models import Student
# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        name=request.POST.get('nm')
        email=request.POST.get('em')
        contact=request.POST.get('con')
        password=request.POST.get('pass')
        cpassword=request.POST.get('cpass')
        #print(name,email,contact,password)
        # Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
        # msg="registraton successfull"
        # return render(request,'home.html',{'msg':msg})
        if password==cpassword:
            user=Student.objects.filter(stu_email=email)
            if user:
                msg="Email already exist"
                return render(request,'register.html',{'msg':msg})
            else:
                Student.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_password=password)
                msg="Registration Successfully"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Password & Confirm Password not matched"
            return render(request,'register.html',{'msg':msg})
    else:
     return render(request,'register.html')

def login(request):
    return render(request,'login.html')