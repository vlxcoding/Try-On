# checkout/models.py
from django.db import models
from appointments.models import Appointment
from inventory.models import Product

class Order(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=20, choices=[("pending", "Pending"), ("paid", "Paid")]
    )
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2)
