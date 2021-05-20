""" Defines URL patterns for tickets. """
from django.urls import path

from . import views

app_name = 'tickets'
urlpatterns = [
    # Home page
    path('', views.index, name ='index'),
    # Page that shows all tickets
    path('tickets/', views.tickets, name='tickets'),
    # Detail page for a single ticket.
    path('tickets/<int:tkt_number>/', views.ticket, name='ticket'),
    # Page for adding a new ticket.
    path('new_ticket/', views.new_ticket, name='new_ticket'),
    # About page.
    path('about', views.about, name='about'),
    # Contact page.
    path('contact', views.contact, name='contact'),
    # Page for editing a new ticket.
    path('edit_ticket/<int:tkt_number>/', views.edit_ticket, name='edit_ticket' ),
]
