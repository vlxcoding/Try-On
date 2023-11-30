# models.py

from django.db import models

class Appointment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # Other fields for your appointment model
