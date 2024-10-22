from django.db import models

# Create your models here.

# class Bookingdata(models.Model):
#     fname=models.CharField(max_length=50)
#     lname=models.CharField(max_length=50)
#     email=models.EmailField()
#     carnm=models.CharField(max_length=50)
#     amount=models.IntegerField()
#     address=models.TextField()
#     pick=models.CharField(max_length=50)
#     drop=models.CharField(max_length=50)
#     feedback=models.TextField()

class User(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    contact=models.IntegerField()