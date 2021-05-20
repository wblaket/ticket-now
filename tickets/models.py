
from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings

# Create your models here.
class Ticket(models.Model):
    """ A single ticket that an end-user can submit."""
    tkt_number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    resolution = models.CharField(max_length=500)
    TICKET_PRIORITY_OPTIONS = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('EMERGENCY', 'Emergency'),
    ]
    ticket_priority = models.CharField(
        max_length=9,
        choices=TICKET_PRIORITY_OPTIONS,
        default='LOW',
    )

    TICKET_STATUS_OPTIONS = [
        ('SUBMITTED', 'Submitted'),
        ('ASSIGNED', 'Assigned'),
        ('IN-PROGRESS', 'In-Progress'),
        ('ON-HOLD', 'On-Hold'),
        ('COMPLETED', 'Completed'),
        ('CLOSED', 'Closed'),
    ]

    tkt_status = models.CharField(
        max_length=12,
        choices=TICKET_STATUS_OPTIONS,
        default='SUBMITTED',
    )
    TICKET_TYPE_OPTIONS = [
        ('INCIDENT', 'Incident'),
        ('REQUEST', 'Request'),
        ('CHANGE', 'Change'),
        ('PROBLEM', 'Problem'),
    ]

    tkt_type = models.CharField(
    max_length=10,
    choices=TICKET_TYPE_OPTIONS,
    default='INCIDENT',
    )

    assignment = models.CharField(max_length=50)



class Meta:
    verbose_name_plural = 'tickets'

def __str__(self):
    """ Return a string representation of the model."""
    return self.text
