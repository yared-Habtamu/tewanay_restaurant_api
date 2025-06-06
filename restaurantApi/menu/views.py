from rest_framework import generics, permissions
from .models import MenuItem
from .serializers import MenuItemSerializer
from users.permissions import IsManager


class MenuItemListView(generics.ListAPIView):#all customers
    queryset = MenuItem.objects.filter(is_available=True)
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]


class MenuItemCreateView(generics.CreateAPIView):  #only for manager and admins
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManager]


class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManager]
