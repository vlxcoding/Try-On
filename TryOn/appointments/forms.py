# appointments/forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time_slot', 'store_location', 'purpose', 'items_to_view', 'notes']
