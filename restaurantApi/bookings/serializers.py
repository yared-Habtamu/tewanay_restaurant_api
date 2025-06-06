from rest_framework import serializers
from .models import TableBooking

class TableBookingSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)  # Show username

    class Meta:
        model = TableBooking
        fields = ['id', 'customer', 'date', 'time', 'guests', 'notes', 'is_confirmed', 'created_at']
        read_only_fields = ['customer', 'created_at']