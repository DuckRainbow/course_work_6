import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail

from mail.models import Mail, MailTry


def get_date_send(mail, current_datetime):
    """
    Функция корректировки  даты и временм для следующей отправки рассылки (datetime_send).
    """
    if mail.datetime_send < current_datetime:
        if mail.periodicity == "daily":
            mail.datetime_send += timedelta(days=1, hours=0, minutes=0)
        elif mail.periodicity == "weekly":
            mail.datetime_send += timedelta(days=7, hours=0, minutes=0)
        elif mail.periodicity == "monthly":
            mail.datetime_send += timedelta(days=30, hours=0, minutes=0)
        mail.save()


def send_mail_by_time():
    """
    Отправка письма по времени, указанному в подписке на рассылку.
    1) Выбираются все актуальные рассылки (status='launched')
    2) Проверяется статус каждой рассылки функцией и соответствие условиям отправки
    3) Формирует emails_list и отправляет письма, сохраняет Лог с информацией об отпрвке
    4) При ошибке отправке формирует лог с этой ошибкой
    """
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mail_list = Mail.objects.all().filter(status='launched')
    if mail_list:
        for mail in mail_list:
            if (
                    mail.datetime_send
                    <= current_datetime
                    <= mail.datetime_finish
            ):
                emails_list = [client.email for client in mail.clients.all()]

                try:
                    server_response = send_mail(
                        subject=mail.message.subject,
                        message=mail.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=emails_list,
                        fail_silently=False,
                    )
                    print("Письмо отправлено")
                    status = "success"
                    mail_try = MailTry(
                        mail=mail,
                        status=status,
                        servers_answer=server_response
                    )
                    mail_try.save()
                    print("попытка сохранена")
                    get_date_send(mail, current_datetime)

                except smtplib.SMTPException as error:
                    status = "fail"
                    server_response = f"Ошибка отправки {error}"
                    mail_try = MailTry(
                        newsletter=mail,
                        status=status,
                        servers_answer=server_response
                    )
                    mail_try.save()
                    print("Попытка с ошибкой отправки", error)

    else:
        print("Нет mail_list")
