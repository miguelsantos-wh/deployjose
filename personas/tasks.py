from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True, queue="deployjose")
def add(self, x, y):
    return x + y


@shared_task(bind=True, queue="deployjose")
def send_mail_persona_update_task(self, nombre='Default'):
    subject = 'Actualización exitosa'
    message = 'Se ha editado exitosamente la persona.'
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['josemiguel@wisphub.net']  # Cambia esto por la dirección de correo electrónico del destinatario
    try:
        send_mail(subject, message, sender_email, recipient_list)
        meta = {'Mensaje enviado': 'El correo se a enviado correctamente'}
    except Exception as e:
        meta = {'Mensaje enviado': F'No se envio el correo. Error: {e}'}
    return meta
