from django.contrib import admin
from .models import PlatformCategory
from .models import IncomeCategory
from .models import ExpenseCategory
from .models import SavingCategory

# Register your models here.
admin.site.register(PlatformCategory)
admin.site.register(IncomeCategory)
admin.site.register(ExpenseCategory)
admin.site.register(SavingCategory)