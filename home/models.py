from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserAdditionalInfo(models.Model): 

    #create ForeignKey so ever list made will link to user
    user = models.OneToOneField(User, default=None, null=True, blank=True, on_delete=models.SET_NULL, unique=True)

    #user_photo = models.ImageField(default='profile_images/teacher_default.png', upload_to="profile_images/")
    profilePicture = models.ImageField(default='static/avatars/dummy.png', upload_to="profile_picture/")

    #define method
    def __str__(self):
        return f"User: {self.user.username}"
    

class PlatformCategory(models.Model): 

    name = models.CharField(max_length=100) #CharField is a type of field that can store information
    description = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name}"
    

class IncomeCategory(models.Model): 
    
    name = models.CharField(max_length=100) #CharField is a type of field that can store information
    description = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name}"
    

class ExpenseCategory(models.Model): 
    
    name = models.CharField(max_length=100) #CharField is a type of field that can store information
    description = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name}"
    
    
class SavingCategory(models.Model): 
    
    name = models.CharField(max_length=100) #CharField is a type of field that can store information
    description = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name}"
    
class DebugCategory(models.Model): 
    
    name = models.CharField(max_length=100) #CharField is a type of field that can store information
    description = models.CharField(max_length=300)
    enabled = models.BooleanField(default=True)

    #create ForeignKey so ever list made will link to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    #define method
    def __str__(self):
        return f"{self.name}"

class IncomeExpenseData(models.Model): 

    transactionDateTime = models.DateTimeField(default=timezone.now) 

    platform = models.ForeignKey(PlatformCategory, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    rawAmount = models.DecimalField(max_digits=10, decimal_places=2)
    currencyChoices = (
        ('THB', 'THB - Thai Baht'),
        ('USD', 'USD - United States Dollar'),
        ('EUR', 'EUR - Euro'),
        ('JYP', 'JYP - Japanese Yen'), 
        ('PHP', 'PHP - Philippine Peso'),
        # Add more currency choices as needed
    )
    rawCurrency = models.CharField(max_length=3, choices=currencyChoices)

    note = models.CharField(max_length=300)

    lastEdit = models.DateTimeField(default=timezone.now)
    lastEditBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  

    #define method
    def __str__(self):
        return f"{self.category}"
    
class AssetData(models.Model): 

    category = models.CharField(max_length=100)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100)

    value_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    currency_choices = (
        ('THB', 'THB - Thai Baht'),
        ('USD', 'USD - United States Dollar'),
        ('EUR', 'EUR - Euro'),
        ('JYP', 'JYP - Japanese Yen'), 
        ('PHP', 'PHP - Philippine Peso'),
        # Add more currency choices as needed
    )
    value_currency = models.CharField(max_length=3, choices=currency_choices)

    note = models.CharField(max_length=500)

    last_edit = models.DateTimeField(default=timezone.now)
    last_edit_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  

    #define method
    def __str__(self):
        return f"{self.category}"

    