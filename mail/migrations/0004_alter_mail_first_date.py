# Generated by Django 4.2.2 on 2024-07-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_alter_mail_first_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='first_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата первой отправки'),
        ),
    ]
