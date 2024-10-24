# from django.db import models

# # Create your models here.


# class User(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.EmailField()
#     contact=models.IntegerField()
#     address=models.TextField()

# quali=[(1,'MTech'),(2,'BTech'),(3,'12th'),(4,'10th')]

# class Profile(models.Model):
#     name=models.OneToOneField(User,on_delete=models.CASCADE)
#     quali=models.CharField(max_length=50,choices=quali)
#     exp=models.IntegerField()
#     skill=models.CharField(max_length=50)
#     other=models.CharField(max_length=50)


from django.db import models

# Create your models here.

class Aadhar(models.Model):
    aadhar=models.IntegerField(primary_key=50)
    def _str_(self):
        return str(self.aadhar)
    
class Department(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_des=models.TextField()
    
    def _str_(self):
        return str(self.dep_name)

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    aadhar_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE)
    department_name=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    
    def _str_(self):
        return str(self.name)
    

quali=((1,"M.Tech"),(2,"B.Tech"),(3,"BCA"),(4,"BBA"))

class Profile(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE)
    quali=models.CharField(max_length=50,choices=quali)
    exp=models.IntegerField()
    skill=models.CharField(max_length=50)