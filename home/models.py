from django.db import models
from django.contrib.auth.models import User


class PlatformCategory(models.Model): 

    name = models.CharField(max_length=100) #CharField is a type of field that can store information
    description = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name} (User: {self.user.username})"
    

class IncomeCategory(models.Model): 
    
    name = models.CharField(max_length=100) #CharField is a type of field that can store information
    description = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name} (User: {self.user.username})"
    

class ExpenseCategory(models.Model): 
    
    name = models.CharField(max_length=100) #CharField is a type of field that can store information
    description = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name} (User: {self.user.username})"
    
    
class SavingCategory(models.Model): 
    
    name = models.CharField(max_length=100) #CharField is a type of field that can store information
    description = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name} (User: {self.user.username})"


class UserAdditionalInfo(models.Model): 

    #create ForeignKey so ever list made will link to user
    user = models.OneToOneField(User, default=None, null=True, blank=True, on_delete=models.SET_NULL, unique=True)

    #user_photo = models.ImageField(default='profile_images/teacher_default.png', upload_to="profile_images/")
    profilePicture = models.ImageField(default='static/avatars/dummy.png', upload_to="profile_picture/")

    #define method
    def __str__(self):
        return f"User: {self.user.username}"