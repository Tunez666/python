from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Customer, MovieSession, Seat, Ticket
from .utils import generate_ticket_pdf
from django.http import HttpResponse


def buy_ticket_view(request):
    if request.method == 'POST':
        # Создание клиента
        customer = Customer.objects.create(
            last_name=request.POST['last_name'],
            first_name=request.POST['first_name'],
            phone=request.POST['phone'],
            birth_date=request.POST['birth_date']
        )

        # Создание билета с выбранным местом
        ticket = Ticket.objects.create(
            customer=customer,
            session_id=request.POST['session_id'],
            seat_id=request.POST['seat_id']
        )
        return redirect('ticket-pdf', ticket_id=ticket.id)

    # GET-запрос: отображение формы
    sessions = MovieSession.objects.all()
    return render(request, 'nursing/buy_ticket.html', {'sessions': sessions})


def free_seats_api(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return JsonResponse({'error': 'session_id parameter is required'}, status=400)

    # Находим свободные места для указанного сеанса
    booked_seats = Ticket.objects.filter(session_id=session_id).values_list('seat_id', flat=True)
    free_seats = Seat.objects.exclude(id__in=booked_seats).values('id', 'number')

    return JsonResponse({
        'seats': list(free_seats)
    })


def ticket_pdf(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    pdf = generate_ticket_pdf(ticket)
    return HttpResponse(pdf, content_type='application/pdf')