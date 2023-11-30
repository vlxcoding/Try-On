# appointments/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm  # Create a forms.py file for handling forms

@login_required
def appointment_schedule(request):
    appointments = Appointment.objects.filter(user=request.user)
    form = AppointmentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Process the form data and create a new appointment
        new_appointment = form.save(commit=False)
        new_appointment.user = request.user
        new_appointment.save()
        form = AppointmentForm()  # Reset the form after successful submission

    context = {
        'appointments': appointments,
        'form': form,
    }
    return render(request, 'appointments/appointment_schedule.html', context)

@login_required
def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)

    context = {
        'appointment': appointment,
    }
    return render(request, 'appointments/appointment_details.html', context)

