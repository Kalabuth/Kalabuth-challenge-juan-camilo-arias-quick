import csv
from io import StringIO
from celery import shared_task
from django.core.mail import EmailMessage
from .models import Clients, Bills
from aplicacion.config.celery import app


@app.task()
def generate_csv_export(email_user):
    clients = Clients.objects.all()

    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerow(['Documento', 'Nombre Completo', 'Cantidad de facturas'])

    for client in clients:
        full_name = client.first_name+ ' '+client.last_name
        number_of_bills = Bills.objects.filter(client=client).count()
        csv_writer.writerow([client.document, full_name, number_of_bills])

    email = EmailMessage(
        'Exportación CSV de Clientes',
        'Por favor, encuentra adjunto el archivo CSV con la lista de clientes.',
        'prueba.quick@outlook.com',
        [email_user],
    )
    email.attach('clientes_exportados.csv', csv_buffer.getvalue(), 'text/csv')
    email.send()