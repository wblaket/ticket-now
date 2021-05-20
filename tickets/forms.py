from django import forms
from  django.contrib.auth.models import User, Group

from .models import Ticket

class TicketForm(forms.ModelForm):

    class Meta:
        TICKET_PRIORITY_OPTIONS = [
            ('LOW', 'Low'),
            ('MEDIUM', 'Medium'),
            ('HIGH', 'High'),
            ('EMERGENCY', 'Emergency'),
        ]

        TICKET_TYPE_OPTIONS = [
            ('INCIDENT', 'Incident'),
            ('REQUEST', 'Request'),
            ('CHANGE', 'Change'),
            ('PROBLEM', 'Problem'),
        ]

        model = Ticket
        fields = ['tkt_type','title', 'desc', 'ticket_priority',]
        labels = {'tkt_type': 'Type', 'title': 'Title', 'desc': 'Description', 'ticket_priority': 'Priority'}
        widgets = {'text': forms.Textarea(attrs={'cols': 90}), 'ticket_priority': forms.Select(choices=TICKET_PRIORITY_OPTIONS),
        'tkt_type':forms.Select(choices=TICKET_TYPE_OPTIONS),}

class EditTicketForm(forms.ModelForm):

    class Meta:
        TICKET_STATUS_OPTIONS = [
            ('SUBMITTED', 'Submitted'),
            ('ASSIGNED', 'Assigned'),
            ('IN-PROGRESS', 'In-Progress'),
            ('ON-HOLD', 'On-Hold'),
            ('COMPLETED', 'Completed'),
            ('CLOSED', 'Closed'),
        ]
        model = Ticket
        fields = [ 'assignment', 'tkt_status', 'resolution']
        labels = { 'assignment': 'Assignment', 'tkt_status': 'Status', 'resolution': 'Resolution/Progress Note',}
        widgets = {'text': forms.Textarea(attrs={'cols': 90}),'tkt_status': forms.Select(choices=TICKET_STATUS_OPTIONS),
        'resolution': forms.Textarea(attrs={'cols': 50}), }
