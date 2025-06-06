from rest_framework import generics, permissions
from .models import TableBooking
from .serializers import TableBookingSerializer
from users.permissions import IsManager, IsCustomer

class TableBookingCreateView(generics.CreateAPIView):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer
    permission_classes = [IsCustomer]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)  # Auto-set the logged-in customer

class AllBookingsListView(generics.ListAPIView):  # only Managers/Admins
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer
    permission_classes = [IsManager]

class MyBookingsListView(generics.ListAPIView):  # ony Customers
    serializer_class = TableBookingSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return TableBooking.objects.filter(customer=self.request.user)