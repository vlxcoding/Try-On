# customer_support/models.py
from django.db import models
from django.contrib.auth.models import User

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
