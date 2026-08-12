from django.shortcuts import render
from django.http import HttpResponse
from costs.models import Expense, Category, Wallet
from django.db.models import Sum
from rest_framework.response import Response
from costs.serializers import ExpenseSerializer, CategorySerializer, WalletSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    def get_queryset(self):
            print("USER:", self.request.user)
            return Expense.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    def get_queryset(self):
        print("user:", self.request.user)
        return Wallet.objects.filter(user= self.request.user)
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

@api_view(["GET"])
def expense_list(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def total_api(request):
    result = Expense.objects.filter(user= request.user).aggregate(Sum("amount"))
    return Response(result)