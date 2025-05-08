
# Chapter 10: Asynchronous Task Processing with Celery

# Example of a Celery task in Django
from celery import shared_task

@shared_task
def send_email(to_email, subject, message):
    # Logic for sending email
    pass
    