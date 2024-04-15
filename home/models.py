from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Platform(models.Model): 

    name = models.CharField(max_length=100) #CharField is a type of field that can store information

    description = models.CharField(max_length=300)

    enable = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name} (User: {self.user.username})"
    
    
# Create your models here.
class UserAdditionalInfo(models.Model): 

    user_photo = models.ImageField(default='profile_images/teacher_default.png', upload_to="profile_images/")

    #create ForeignKey so ever list made will link to user
    user = models.OneToOneField(User, default=None, null=True, blank=True, on_delete=models.SET_NULL, unique=True)


    #define method
    def __str__(self):
        return f"{self.name} (User: {self.user.username})"