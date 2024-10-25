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


class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    def __str__(self):
        return str(self.name)
    

quali=[("1","M.Tech"),("2","B.Tech"),("3","BCA"),("4","BBA")]

class Profile(models.Model):
    pro_name=models.OneToOneField(User,on_delete=models.CASCADE)
    quali=models.CharField(max_length=50,choices=quali)
    city=models.CharField(max_length=50)
    def __str__(self):
        return str(self.pro_name)
