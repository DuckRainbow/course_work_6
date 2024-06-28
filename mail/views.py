from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mail.models import Client, MailMessage, Mail, MailTry


class ClientListView(ListView):
    model = Client

    # def get_queryset(self):
    # return get_products_from_cache()


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView, LoginRequiredMixin):
    model = Client
    # form_class = ClientForm
    # success_url = reverse_lazy('catalog:products_list')

    # def form_valid(self, form):
    #     product = form.save()
    #     user = self.request.user
    #     product.creator = user
    #     product.save()
    #     return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    # form_class = ClientForm
    # success_url = reverse_lazy('catalog:products_list')

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     ProductFormSet = inlineformset_factory(Product, Version, VersionForm, extra=1)
    #     if self.request.method == 'POST':
    #         context_data['formset'] = ProductFormSet(self.request.POST, instance=self.object)
    #     else:
    #         context_data['formset'] = ProductFormSet(instance=self.object)
    #     return context_data
    #
    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     formset = context["formset"]
    #     self.object = form.save()
    #     if formset.is_valid():
    #         formset.instance = self.object
    #         formset.save()
    #     else:
    #         return self.form_invalid(form)
    #     return super().form_valid(form)

    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.creator:
    #         return ProductForm
    #     if user.has_perm('catalog.can_publish_product') and user.has_perm(
    #             'catalog.can_edit_description') and user.has_perm(
    #             'catalog.can_change_category'):
    #         return ProductModeratorForm
    #     raise PermissionDenied


class ClientDeleteView(DeleteView):
    model = Client
    # success_url = reverse_lazy('catalog:products_list')


class MailMessageListView(ListView):
    model = MailMessage


class MailMessageDetailView(DetailView):
    model = MailMessage

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_counter += 1
    #     self.object.save()
    #     return self.object


class MailMessageCreateView(CreateView):
    model = MailMessage
    # success_url = reverse_lazy('catalog:articles_list')


class MailMessageUpdateView(UpdateView):
    model = MailMessage
    # fields = ('title', 'slug', 'content', 'preview', 'published')
    # success_url = reverse_lazy('catalog:articles_list')

    # def get_success_url(self):
    #     return reverse('catalog:articles_detail', args=[self.kwargs.get('pk')])


class MailMessageDeleteView(DeleteView):
    model = MailMessage
    # success_url = reverse_lazy('catalog:articles_list')


class MailListView(ListView):
    model = Mail


class MailDetailView(DetailView):
    model = Mail

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_counter += 1
    #     self.object.save()
    #     return self.object


class MailCreateView(CreateView):
    model = Mail
    # success_url = reverse_lazy('catalog:articles_list')


class MailUpdateView(UpdateView):
    model = Mail
    # fields = ('title', 'slug', 'content', 'preview', 'published')
    # success_url = reverse_lazy('catalog:articles_list')

    # def get_success_url(self):
    #     return reverse('catalog:articles_detail', args=[self.kwargs.get('pk')])


class MailDeleteView(DeleteView):
    model = Mail
    # success_url = reverse_lazy('catalog:articles_list')


class MailTryListView(ListView):
    model = MailTry


class MailTryDetailView(DetailView):
    model = MailTry

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_counter += 1
    #     self.object.save()
    #     return self.object


class MailTryCreateView(CreateView):
    model = MailTry
    # success_url = reverse_lazy('catalog:articles_list')


class MailTryUpdateView(UpdateView):
    model = MailTry
    # fields = ('title', 'slug', 'content', 'preview', 'published')
    # success_url = reverse_lazy('catalog:articles_list')

    # def get_success_url(self):
    #     return reverse('catalog:articles_detail', args=[self.kwargs.get('pk')])


class MailTryDeleteView(DeleteView):
    model = MailTry
    # success_url = reverse_lazy('catalog:articles_list')
