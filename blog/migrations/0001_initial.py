# Generated by Django 4.2.2 on 2024-07-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Введите заголовок статьи.', max_length=50, null=True, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, help_text='Введите URL статьи.', max_length=100, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, help_text='Введите статью.', null=True, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, help_text='Добавьте изображение.', null=True, upload_to='catalog/image', verbose_name='Превью статьи')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')),
                ('published', models.BooleanField(blank=True, verbose_name='Опубликована')),
                ('views_counter', models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Счетчик просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
