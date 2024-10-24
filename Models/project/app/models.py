from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_password=models.CharField(max_length=25)

class Query(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_query=models.TextField()
    def __str__(self):
        return self.stu_query

        

    
class Aadhar(models.Model):
    aadhar=models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.aadhar)
class Department(models.Model):
    departmentname=models.CharField(max_length=50)
    discraption=models.TextField()
    def __str__(self):
        return str(self.departmentname)

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    aadhar_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE)
    departmentname=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)


quali=((1,"M.Tech"),(2,"B.Tech"),(3,"BCA"),(4,"BBA"))
class Profile(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE)
    quali=models.CharField(max_length=50,choices=quali)
    exp=models.IntegerField()
    skill=models.CharField(max_length=50)