from django import forms
from django.forms import BooleanField

from mail.models import Mail


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MailForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('title', 'first_date', 'periodicity', 'status', 'mail_message', 'client')


