from django.urls import path
from .views import OrderCreateView, OrderListView, MyOrdersView

urlpatterns = [
    path('order/', OrderCreateView.as_view(), name='order-create'),  # POSTcustomer
    path('all/', OrderListView.as_view(), name='order-list'),  # GET for manager and Admin
    path('mine/', MyOrdersView.as_view(), name='my-orders'),   # GET only for customers
]