from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm


def generate_ticket_pdf(ticket):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A5)
    width, height = A5

    # Заголовок
    p.setFont("Helvetica-Bold", 16)
    p.drawString(20 * mm, height - 20 * mm, "Cinema 'CINEMA'")

    # Информация о фильме
    p.setFont("Helvetica", 12)
    p.drawString(20 * mm, height - 35 * mm, f"Movie: {ticket.session.title}")
    p.drawString(20 * mm, height - 45 * mm, f"Start: {ticket.session.start_time.strftime('%d.%m.%Y %H:%M')}")

    # Информация о месте
    p.drawString(20 * mm, height - 60 * mm, f"Seat: {ticket.seat.number}")

    # Информация о покупателе
    p.drawString(20 * mm, height - 75 * mm, f"Customer: {ticket.customer.last_name} {ticket.customer.first_name}")
    p.drawString(20 * mm, height - 85 * mm, f"Number of phone: {ticket.customer.phone}")

    # QR-код (заглушка)
    p.drawString(20 * mm, height - 120 * mm, "QR-code")

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer