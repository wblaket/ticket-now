from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm, EditTicketForm
from  django.contrib.auth.models import User, Group
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    """ The home page. """
    return render(request, 'tickets/index.html')

def about(request):
    """ The about page. """
    return render(request, 'tickets/about.html')

def contact(request):
    """ The contact page. """
    return render(request, 'tickets/contact.html')

def is_tech(user):
    """ Check and see if the user is a member of the technican group."""
    return user.groups.filter(name='Technican').exists()

@login_required
def tickets(request):
    """ Show all tickets. """
    # Query the database for all tickets, sort by date added.
    if (is_tech(request.user)):
        tickets = Ticket.objects.order_by('date_added')
    else:
        tickets = Ticket.objects.filter(owner=request.user).order_by('date_added')
    context = {'tickets': tickets}
    return render(request, 'tickets/tickets.html', context)

@login_required
def ticket(request, tkt_number):
    """ Show a single ticket and all its details."""
    ticket = Ticket.objects.get(tkt_number = tkt_number)
    if ticket.owner != request.user:
        if (is_tech(request.user) == 'false'):
            raise Http404
    context = {'ticket': ticket}
    return render(request, 'tickets/ticket.html', context)

@login_required
def new_ticket(request):
    """ Submit a new ticket. """
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TicketForm()
    else:
        # POST data submitted; process data.
        form = TicketForm(data=request.POST)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.owner = request.user
            new_ticket.save()
            return redirect('tickets:tickets')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'tickets/new_ticket.html', context)

@login_required
def edit_ticket(request, tkt_number):
    """ Edit existing ticket. """
    ticket = Ticket.objects.get(tkt_number=tkt_number)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
         form = EditTicketForm(instance=ticket)
    else:
        # POST data submitted; process data.
        form = EditTicketForm(instance=ticket, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets:ticket', tkt_number=tkt_number)
    context = {'ticket': ticket, 'form': form}
    return render(request, 'tickets/edit_ticket.html', context)
