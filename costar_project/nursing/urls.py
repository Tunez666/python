from django.urls import path
from .views import buy_ticket_view, ticket_pdf, free_seats_api

urlpatterns = [
    path('buy/', buy_ticket_view, name='buy-ticket'),
    path('ticket/<int:ticket_id>/pdf/', ticket_pdf, name='ticket-pdf'),
    path('api/free-seats/', free_seats_api, name='free-seats-api'),
]