from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Customeuser(AbstractUser):
    USER=(
        ('1','HOD'),
        ('2', 'STAFF'),
        ('3', 'STUDENT'),
    )
    user_Type=models.CharField(choices=USER,max_length=50,default=1)
    profilepic=models.ImageField(upload_to='media/profilepic')

# class Cource(models.Model):
#     name=models.CharField(max_length=100)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
class Sessionyear(models.Model):
    sessionstart=models.CharField(max_length=100)
    sessionend=models.CharField(max_length=100)
    def __str__(self):
        return self.sessionstart    +  " to " + self.sessionend

class Student(models.Model):
    admin=models.OneToOneField(Customeuser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=100)
    course=models.CharField(max_length=100,blank=True)
    session_year_id=models.ForeignKey(Sessionyear,on_delete=models.DO_NOTHING)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.admin.first_name + "" + self.admin.last_name

    
