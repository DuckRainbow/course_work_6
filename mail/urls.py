from django.urls import path
from mail.apps import MailConfig
from mail.views import MailListView, MailDetailView, MailCreateView, MailUpdateView, MailDeleteView, ClientListView, \
    ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, MailMessageListView, MailMessageDetailView, \
    MailMessageCreateView, MailMessageUpdateView, MailMessageDeleteView, MailTryListView

app_name = MailConfig.name

urlpatterns = [
    path('', MailListView.as_view(), name='mails_list'),
    path('mail/<int:pk>/', MailDetailView.as_view(), name='mails_detail'),
    path('mail/create/', MailCreateView.as_view(), name='mails_create'),
    path('mail/<int:pk>/update/', MailUpdateView.as_view(), name='mails_update'),
    path('mail/<int:pk>/delete/', MailDeleteView.as_view(), name='mails_delete'),
    path('сlients', ClientListView.as_view(), name='clients_list'),
    path('сlients/<int:pk>/', ClientDetailView.as_view(), name='clients_detail'),
    path('сlients/create/', ClientCreateView.as_view(), name='clients_create'),
    path('сlients/<int:pk>/update/', ClientUpdateView.as_view(), name='clients_update'),
    path('сlients/<int:pk>/delete/', ClientDeleteView.as_view(), name='clients_delete'),
    path('messages', MailMessageListView.as_view(), name='messages_list'),
    path('messages/<int:pk>/', MailMessageDetailView.as_view(), name='messages_detail'),
    path('messages/create/', MailMessageCreateView.as_view(), name='messages_create'),
    path('messages/<int:pk>/update/', MailMessageUpdateView.as_view(), name='messages_update'),
    path('messages/<int:pk>/delete/', MailMessageDeleteView.as_view(), name='messages_delete'),
    path('mailtries', MailTryListView.as_view(), name='mailtry_list'),
]
