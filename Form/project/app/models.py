from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    address=models.TextField()

quali=[(1,'MTech'),(2,'BTech'),(3,'12th'),(4,'10th')]

class Profile(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE)
    quali=models.CharField(max_length=50,choices=quali)
    exp=models.IntegerField()
    skill=models.CharField(max_length=50)
    other=models.CharField(max_length=50)