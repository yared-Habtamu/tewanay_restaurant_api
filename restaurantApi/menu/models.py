from django.db import models


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('APPETIZER', 'Appetizer'),
        ('MAIN', 'Main Course'),
        ('DESSERT', 'Dessert'),
        ('BEVERAGE', 'Beverage'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (${self.price})"
