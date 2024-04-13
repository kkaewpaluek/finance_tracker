from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Platform(models.Model): 

    name = models.CharField(max_length=100) #CharField is a type of field that can store information

    description = models.CharField(max_length=300)

    enable = models.BooleanField()

    #create ForeignKey so ever list made will link to user
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) 

    #define method
    def __str__(self): #'__str__' is to set text representation
        return self.name #for example -> if print then return 'name'