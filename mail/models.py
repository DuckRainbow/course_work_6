from django.db import models


class Client(models.Model):
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
    )
    full_name = models.CharField(
        max_length=50,
        verbose_name="Ф.И.О",
        blank=True,
        null=True,
        help_text='Введите ФИО клиента.'
    )
    comment = models.CharField(
        max_length=100,
        verbose_name="комментарий",
        blank=True,
        null=True,
        help_text='Введите комментарий к клиенту.'
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.full_name}, email - {self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Mail(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название",
        blank=True,
        null=True,
        help_text='Введите название рассылки.'
    )
    first_date = models.DateTimeField(
        verbose_name="Дата создания",
        blank=True,
        null=True
    )
    MAIL_PERIODICITY = (
        ('one_a_day', 'Ежедневная рассылка'),
        ('one_a_week', 'Еженедельная рассылка'),
        ('one_a_month', 'Ежемесячная рассылка'),
    )
    periodicity = models.CharField(
        max_length=20,
        choices=MAIL_PERIODICITY,
        verbose_name="Периодичность рассылки",
        blank=True,
        null=True,
        help_text='Выберите периодичность.'
    )
    MAIL_STATUS = (
        ('created', 'Создана'),
        ('launched', 'Запущена'),
        ('completed', 'Завершена'),
    )
    status = models.CharField(
        max_length=20,
        choices=MAIL_STATUS,
        verbose_name="Cтатус рассылки",
        blank=True,
        null=True,
        help_text='Выберите статус.'
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.full_name}, email - {self.email}"

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
