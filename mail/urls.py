from django.urls import path
from mail.apps import MailConfig
from mail.views import MailListView

app_name = MailConfig.name

urlpatterns = [
    path('', MailListView.as_view(), name='mail_list'),
]
