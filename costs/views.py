from django.shortcuts import render
from django.http import HttpResponse
from costs.models import Expense
from django.db.models import Sum

def hello(request):
    expenses = Expense.objects.all()
    text = ""
    for e in expenses:
        text += f"{e.note} - {e.amount}<br>"
    return HttpResponse(text)

def total(request):
    result = Expense.objects.aggregate(Sum("amount"))
    return HttpResponse(result["amount__sum"])

