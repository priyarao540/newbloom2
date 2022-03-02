# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255,default="mukesh")
    email = models.CharField(max_length=255,unique=True)
    phone  = models.CharField(max_length=15,default="987654321")
    
    def __str__(self) :
        return self.email +" " + self.name + " "


class Books(models.Model):
    student = models.ForeignKey(to=User,on_delete=models.CASCADE)
    b_name = models.CharField(max_length=255,default="story")
    b_number  = models.CharField(max_length=150,default="987654321")
    
    def __str__(self) :
        return self.b_name +" " + self.b_number + " "



    

# Models => Migrations => Sql
