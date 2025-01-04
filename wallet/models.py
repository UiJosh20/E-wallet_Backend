from django.db import models

class LinkedAccount(models.Model):
    name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    linked_account = models.ForeignKey(LinkedAccount, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    TRANSACTION_TYPES = (('income', 'Income'), ('expense', 'Expense'))
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateTimeField(auto_now_add=True)

class QRTransaction(models.Model):
    qr_code = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_received = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
