from django.contrib import admin

from mail.models import Client, MailMessage, Mail


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email')
    search_fields = ('email', 'full_name')


@admin.register(MailMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'body')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'first_date', 'periodicity', 'status')
    list_filter = ('status', 'periodicity')
    search_fields = ('title', 'first_date')
