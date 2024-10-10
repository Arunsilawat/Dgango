from django.shortcuts import render
from.models import Student
from.models import Query

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

# def login(request):
#     return render(request,'login.html')
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        # print(email,password)
        use=Student.objects.filter(stu_email=email)
        # print(use)
        if use:
            use_data=Student.objects.get(stu_email=email)
            # print(use_data)
            email1=use_data.stu_email
            name1=use_data.stu_name
            contact1=use_data.stu_contact 
            password1=use_data.stu_password
            # print(email1,name1,contact1,password1)
            if password1==password:
                data={
                    'nm':name1,
                    'em':email1,
                    'con':contact1,
                    'pas':password1
                }
                return render(request,'display.html',{'user':data})
            else:
                msg="Password Not Match"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email Id not Register"
            return render(request,'login.html',{'msg':msg})        
    else:
        return render(request,'login.html')
def first(request):
    data=Student.objects.first()
    # print(data)
    # print(data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    data1={
        'nm':data.stu_name,
        'em':data.stu_email,
        'con':data.stu_contact,
        'pas':data.stu_password
        }

    return render(request,'dashboard.html',data1)
def last(request):
    data=Student.objects.last()
    # print(data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    data1={
    'nm':data.stu_name,
    'em':data.stu_email,
    'con':data.stu_contact,
    'pas':data.stu_password
    }
    return render(request,'dashboard.html',data1)
def latest(request):
    data=Student.objects.latest("id")
    print(data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    data1={
    'nm':data.stu_name,
    'em':data.stu_email,
    'con':data.stu_contact,
    'pas':data.stu_password
    }
    return render(request,'dashboard.html',data1) 
def earliest(request):
    data=Student.objects.earliest("id")
    print(data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    data1={
    # 'id':data.stu_id,
    'nm':data.stu_name,
    'em':data.stu_email,
    'con':data.stu_contact,
    'pas':data.stu_password
    }
    return render(request,'dashboard.html',data1)
# ------------------------------multiple return-----------------------------------------------

def all(request):
    data=Student.objects.all()
    data1=data.values()
    return render(request,'dashboard.html',{'data':data1})

def myfilter(request):
    data=Student.objects.filter(stu_name="Arun")
    data1=data.values()
    return render(request,'dashboard.html',{'data':data1})

def myexclude(request):
    data=Student.objects.exclude(stu_name="Arun")
    data1=data.values()
    return render(request,'dashboard.html',{'data':data1})

def myassending(request):
    data=Student.objects.order_by("stu_name")  #  .reverse()  se bhi dissending de dega
    data1=data.values()
    return render(request,'dashboard.html',{'data':data1})

def mydissending(request):
    data=Student.objects.order_by("-stu_name")
    data1=data.values()
    return render(request,'dashboard.html',{'data':data1})

def myrendom(request):
    data=Student.objects.order_by("?")
    data1=data.values()
    return render(request,'dashboard.html',{'data':data1})

def myslice(request):
    data=Student.objects.all()[5::]
    data1=data
    return render(request,'dashboard.html',{'data':data1})

def myreverse(request):
    data=Student.objects.order_by("-id")[:5:]
    data1=data.values()
    return render(request,'dashboard.html',{'data':data})

# ----------------------------------------------------------------------
# def query(request):
#     if request.method=="POST":
#         name1=request.POST.get('name')
#         email1=request.POST.get('email')
#         contact1=request.POST.get('contact')
#         query=request.POST.get('query')
#         Query.objects.create(name=name1,email=email1,contact=contact,query=query)
#         data=Student.objects.get(stu_email=email1)
#         return render(request,'display.html',{'data':data})

def query(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        query=request.POST.get('query')
        Query.objects.create(stu_name=name,stu_email=email,stu_contact=contact,stu_query=query)
        msg=" Successfully"
        data1=Query.objects.filter(stu_email=email)
        # data1=data.values()
        use_data=Student.objects.get(stu_email=email)
        email1=use_data.stu_email
        name1=use_data.stu_name
        contact1=use_data.stu_contact 
        password1=use_data.stu_password
        data={
            'nm':name1,
            'em':email1,
            'con':contact1,
            'pas':password1
            }
        return render(request,'display.html',{'data':data1,'user':data})
    else:
        msg=" not success"
        return render(request,'register.html',{'msg':msg})
def delete(request,pk,em):
    data=Query.objects.filter(id=pk)
    if data:
        data=Query.objects.get(id=pk)
        email=data.stu_email
        data.delete()
        alldata=Query.objects.filter(stu_email=email)
        use_data=Student.objects.get(stu_email=email)
        email1=use_data.stu_email
        name1=use_data.stu_name
        contact1=use_data.stu_contact 
        password1=use_data.stu_password
        data={
            'nm':name1,
            'em':email1,
            'con':contact1,
            'pas':password1
            }
        return render(request,'display.html',{'data':alldata,'user':data})
    else:
        alldata=Query.objects.filter(stu_email=em)
        use_data=Student.objects.get(stu_email=em)
        email1=use_data.stu_email
        name1=use_data.stu_name
        contact1=use_data.stu_contact 
        password1=use_data.stu_password
        data={
            'nm':name1,
            'em':email1,
            'con':contact1,
            'pas':password1
            }
        return render(request,'display.html',{'data':alldata,'user':data})

def logout(request):
    return render(request,'home.html')
  
def edit(request,pk):
    data=Query.objects.get(id=pk)
    myid=data.id
    name=data.stu_name
    email=data.stu_email
    contact=data.stu_contact
    query=data.stu_query
    
    alldata=Query.objects.filter(stu_email=email)
    use_data=Student.objects.get(stu_email=email)

    email1=use_data.stu_email
    name1=use_data.stu_name
    contact1=use_data.stu_contact 
    password1=use_data.stu_password
    data={
        'myid':myid,
        'nm':name1,
        'em':email1,
        'con':contact1,
        'query':query
        }
    edit_detail={
        'nm':name,
        'em':email,
        'con':contact,
        'query':query
    }
    return render(request,'display.html',{'data':alldata,'user':data,'key2':edit_detail})
def update(request,pk):
    if request.method=='POST':
        old_data=Query.objects.get(id=pk)
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        query=request.POST.get("query")

        old_data.stu_name=name 
        old_data.stu_email=email
        old_data.stu_contact=contact
        old_data.stu_query=query
        old_data.save()

        alldata=Query.objects.filter(stu_email=email)
        use_data=Student.objects.get(stu_email=email)

        email1=use_data.stu_email
        name1=use_data.stu_name
        contact1=use_data.stu_contact 
        password1=use_data.stu_password
        data={
            'nm':name1,
            'em':email1,
            'con':contact1,
            'query':query
            }
        return render(request,'display.html',{'data':alldata,'user':data})