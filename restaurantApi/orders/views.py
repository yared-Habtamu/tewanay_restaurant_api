from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer
from users.permissions import IsManager, IsCustomer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsCustomer]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class OrderListView(generics.ListAPIView):  # For Managers& Admins
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsManager]


class MyOrdersView(generics.ListAPIView):  #For Customers
    serializer_class = OrderSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
