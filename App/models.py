from django.db import models
class Login(models.Model):
    Source=models.CharField(max_length=20)
    Name=models.CharField(max_length=30)
    Category=models.CharField(max_length=20)
    Password=models.CharField(max_length=20,default="Manasa@123")


# Create your models here.
