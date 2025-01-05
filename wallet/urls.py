from django.urls import path
from .views import DataView

urlpatterns = [
     path('TransactionData', DataView.as_view(), name='TransactionData'),
]
