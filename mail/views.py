import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from config.settings import CACHE_ENABLED
from mail.forms import ClientForm, MailMessageForm, MailForm
from mail.models import Client, MailMessage, Mail, MailTry
from blog.services import get_articles_from_cache


class ClientListView(ListView):
    model = Client

    @staticmethod
    def get_clients_from_cache():
        """Получает данные из кэша, если кэш пуст, получает данные из бд."""
        if not CACHE_ENABLED:
            return Client.objects.all()
        key = 'clients_list'
        clients = cache.get(key)
        if clients is not None:
            return clients
        clients = Client.objects.all()
        cache.set(key, clients)
        return clients


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ClientForm
        # if user.has_perm('catalog.can_publish_product') and user.has_perm(
        #         'catalog.can_edit_description') and user.has_perm(
        #         'catalog.can_change_category'):
        #     return ClientForm
        raise PermissionDenied


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mail:clients_list')


class MailMessageListView(ListView):
    model = MailMessage


class MailMessageDetailView(DetailView):
    model = MailMessage


class MailMessageCreateView(CreateView):
    model = MailMessage
    form_class = MailMessageForm
    success_url = reverse_lazy('mail:messages_list')


class MailMessageUpdateView(UpdateView):
    model = MailMessage
    form_class = MailMessageForm

    def get_success_url(self):
        return reverse('mail:messages_detail', args=[self.kwargs.get('pk')])


class MailMessageDeleteView(DeleteView):
    model = MailMessage
    success_url = reverse_lazy('mail:messages_list')


class MailListView(ListView):
    model = Mail


class MailDetailView(DetailView):
    model = Mail


class MailCreateView(CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mail:mails_list')


class MailUpdateView(UpdateView):
    model = Mail
    form_class = MailForm

    def get_success_url(self):
        return reverse('mail:mails_detail', args=[self.kwargs.get('pk')])


class MailDeleteView(DeleteView):
    model = Mail
    success_url = reverse_lazy('mail:mails_list')


class MailTryListView(ListView):
    model = MailTry


class HomePage(TemplateView):
    template_name = 'mail/index.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['mail_count'] = Mail.objects.all().count()
        context_data['active_mail_count'] = Mail.objects.exclude(status='completed').count()
        context_data['clients_count'] = Client.objects.all().count()
        articles = self.get_articles_from_cache()
        random.shuffle(articles)
        context_data['some_articles'] = articles[0:3]
        return context_data
