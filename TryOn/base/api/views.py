from django.shortcuts import render

# Create your views here.
# customer_support/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from base.models import Ticket
from base.forms import TicketForm

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'customer_support/ticket_list.html', {'tickets': tickets})

@login_required
def ticket_details(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    return render(request, 'customer_support/ticket_details.html', {'ticket': ticket})

@login_required
def create_ticket(request):
    form = TicketForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        new_ticket = form.save(commit=False)
        new_ticket.user = request.user
        new_ticket.save()
        form = TicketForm()

    return render(request, 'customer_support/create_ticket.html', {'form': form})

def tickets_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'customer_support/tickets_list.html', {'tickets': tickets})

def ticket_details(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'customer_support/ticket_details.html', {'ticket': ticket})

# appointments/views.py



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

