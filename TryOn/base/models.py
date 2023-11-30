
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
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



class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20, choices=[("open", "Open"), ("closed", "Closed")]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.user.username}: {self.subject}"
    



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

