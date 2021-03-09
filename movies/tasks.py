from celery import shared_task
from django.core.mail import mail_admins


@shared_task(autoretry_for=(Exception,))
def send_mail_to_admins(message):
  mail_admins(
    'Created new movie',
    message,
    fail_silently=False,
  )