# customer_support/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm

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