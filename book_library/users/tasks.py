from celery import shared_task
from django.core.mail import send_mail

from book_library.settings import EMAIL_HOST_USER


@shared_task
def send_welcome_email(user_email):
    subject = 'Добро пожаловать!'
    message = 'Ваша регистрация прошла успешно. Добро пожаловать в библиотеку!'
    from_email = EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
