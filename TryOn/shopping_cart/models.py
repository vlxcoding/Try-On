# shopping_cart/models.py
from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product  # Import the Product model from the inventory app

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate subtotal price before saving
        self.subtotal_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.user.username}"
