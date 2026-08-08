from django.contrib import admin

# Register your models here.
from django.contrib import admin
from costs.models import Category, Expense, Wallet

admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Wallet)