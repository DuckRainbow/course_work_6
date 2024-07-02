from time import sleep

from django.apps import AppConfig

from mail.services import send_mail_by_time


class MailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail'

    def ready(self):
        sleep(2)
        send_mail_by_time()
