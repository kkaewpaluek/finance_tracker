from django.contrib import admin
from .models import PlatformCategory
from .models import IncomeCategory
from .models import ExpenseCategory
from .models import SavingCategory
from .models import DebugCategory
from .models import IncomeExpenseData
from .models import AssetData

# Register your models here.
admin.site.register(PlatformCategory)
admin.site.register(IncomeCategory)
admin.site.register(ExpenseCategory)
admin.site.register(SavingCategory)
admin.site.register(DebugCategory)
admin.site.register(IncomeExpenseData)
admin.site.register(AssetData)