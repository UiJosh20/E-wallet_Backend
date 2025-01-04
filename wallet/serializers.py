from rest_framework import serializers
from .models import LinkedAccount, Transaction, QRTransaction

class LinkedAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedAccount
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class QRTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRTransaction
        fields = '__all__'
