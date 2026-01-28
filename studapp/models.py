from django.db import models

# Create your models here.
class Studentdb(models.Model):
    studId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)#duplicate shift + alt +up/down
    course=models.CharField(max_length=100,null=True,blank=True)#duplicate shift + alt +up/down
    mobile=models.IntegerField(null=True,blank=True)#duplicate shift + alt +up/down