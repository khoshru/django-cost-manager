from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Expense(models.Model):
    amount = models.IntegerField()
    note = models.CharField(max_length=200)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.amount} - {self.note} - {self.date}"

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    wallet = models.CharField(max_length=200)
    inventory = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.inventory}"
