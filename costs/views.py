from django.shortcuts import render
from django.http import HttpResponse
from costs.models import Expense, Category
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from costs.serializers import ExpenseSerializer, CategorySerializer
from rest_framework import viewsets


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def hello(request):
    expenses = Expense.objects.all()
    text = ""
    for e in expenses:
        text += f"{e.note} - {e.amount}<br>"
    return HttpResponse(text)

def total(request):
    result = Expense.objects.aggregate(Sum("amount"))
    return HttpResponse(result["amount__sum"])

@api_view(["GET"])
def expense_list(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def total_api(request):
    result = Expense.objects.aggregate(Sum("amount"))
    return Response(result)