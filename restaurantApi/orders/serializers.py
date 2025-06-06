from rest_framework import serializers
from .models import Order, OrderItem
from menu.serializers import MenuItemSerializer  # Reuse menu serializer
from menu.models import MenuItem

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(),
        source='menu_item',
        write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_id', 'quantity', 'special_requests']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    customer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'items', 'created_at', 'updated_at']
        read_only_fields = ['status', 'customer']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order