# appointments/models.py
from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product  # Ensure correct import path for Product model

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    store_location = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20, choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Additional fields based on your requirements
    purpose = models.TextField(blank=True, null=True)
    items_to_view = models.ManyToManyField(Product, related_name='appointments', blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment {self.id} - {self.user.username} on {self.date} at {self.time_slot}"
