from django.contrib.auth.models import User
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


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data["username"],
            email = validated_data["email"],
            password = validated_data["password"]
        )
        return user