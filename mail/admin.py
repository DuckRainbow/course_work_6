from django.contrib import admin

from mail.models import Client, MailMessage, Mail


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'owner')
    list_filter = ('owner',)
    search_fields = ('email', 'full_name', 'owner')


@admin.register(MailMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'body', 'owner')
    list_filter = ('owner',)
    search_fields = ('subject', 'owner')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'first_date', 'periodicity', 'status', 'mail_message', 'clients', 'owner')
    list_filter = ('owner', 'clients', 'mail_message', 'status', 'periodicity')
    search_fields = ('title', 'first_date', 'owner')
