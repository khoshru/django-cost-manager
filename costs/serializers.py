from rest_framework import serializers
from costs.models import Expense, Category, Wallet


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "amount", "note", "date", "category"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ["id", "name"]

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "wallet", "inventory"]       