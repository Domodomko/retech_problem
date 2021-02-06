# Django
from django.urls import path

# local Django
from .views import *

urlpatterns = [
    path('vendinglist/', VendingListView.as_view(), name='clinic'),
    path('vendingbuy/', VendingBuyView.as_view(), name='buy'),
    path('vendingfill/', VendingFillView.as_view(), name='fill'),
    path('vendingfill/',VendingEmptyListView.as_view(), name='fill'),
]