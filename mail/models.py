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


class MailMessage(models.Model):
    subject = models.CharField(
        max_length=100,
        verbose_name="Тема письма",
        blank=True,
        null=True,
        help_text='Введите тему письма.'
    )
    body = models.TextField(
        verbose_name="Тело письма",
        blank=True,
        null=True,
        help_text='Введите текст письма.'
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.subject}"

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"


class MailTry(models.Model):
    date_time = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время последней попытки",
        blank=True,
        null=True
    )
    TRY_STATUS = (
        ('success', 'Успешно'),
        ('fail', 'Не успешно'),
    )
    status = models.CharField(
        max_length=20,
        choices=TRY_STATUS,
        verbose_name="Cтатус попытки",
        blank=True,
        null=True
    )
    servers_answer = models.CharField(
        max_length=100,
        verbose_name="Ответ сервера",
        blank=True,
        null=True,
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.date_time}, {self.status}"

    class Meta:
        verbose_name = "попытка"
        verbose_name_plural = "попытки"
