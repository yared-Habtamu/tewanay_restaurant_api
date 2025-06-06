from django.db import models
from users.models import User


class TableBooking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()  # Number of guests
    notes = models.TextField(blank=True)  # Special requests
    is_confirmed = models.BooleanField(default=True)  # Manager can toggle
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} for {self.guests} guests on {self.date} at {self.time}"
