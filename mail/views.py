import random

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blog.models import Article
from config.settings import CACHE_ENABLED
from mail.forms import ClientForm, MailMessageForm, MailForm, MailModeratorForm
from mail.models import Client, MailMessage, Mail, MailTry


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ClientForm
        raise PermissionDenied


class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mail:clients_list')


class MailMessageListView(ListView):
    model = MailMessage


class MailMessageDetailView(DetailView):
    model = MailMessage


class MailMessageCreateView(PermissionRequiredMixin, CreateView):
    model = MailMessage
    form_class = MailMessageForm
    success_url = reverse_lazy('mail:messages_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class MailMessageUpdateView(PermissionRequiredMixin, UpdateView):
    model = MailMessage
    form_class = MailMessageForm

    def get_success_url(self):
        return reverse('mail:messages_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailMessageForm
        raise PermissionDenied


class MailMessageDeleteView(PermissionRequiredMixin, DeleteView):
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

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class MailUpdateView(UpdateView):
    model = Mail
    form_class = MailForm

    def get_success_url(self):
        return reverse('mail:mails_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailForm
        if user.has_perm('mail.can_see_mails') and user.has_perm(
                'mail.can_change_status'):
            return MailModeratorForm
        raise PermissionDenied


class MailDeleteView(DeleteView):
    model = Mail
    success_url = reverse_lazy('mail:mails_list')


class MailTryListView(ListView):
    model = MailTry


class HomePage(TemplateView):
    template_name = 'mail/index.html'

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

    @staticmethod
    def get_articles_from_cache():
        """Получает данные из кэша, если кэш пуст, получает данные из бд."""
        if not CACHE_ENABLED:
            return Article.objects.all()
        key = 'articles_list'
        articles = cache.get(key)
        if articles is not None:
            return articles
        articles = Article.objects.all()
        cache.set(key, articles)
        return articles

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['mail_count'] = Mail.objects.all().count()
        context_data['active_mail_count'] = Mail.objects.exclude(status='completed').count()
        context_data['clients_count'] = len(self.get_clients_from_cache())
        articles = self.get_articles_from_cache()
        random.shuffle(articles)
        context_data['some_articles'] = articles[0:3]
        return context_data
