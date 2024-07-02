from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        blank=True,
        null=True,
        help_text='Введите заголовок статьи.'
    )
    slug = models.CharField(
        max_length=100,
        verbose_name="slug",
        blank=True,
        null=True,
        help_text='Введите URL статьи.'
    )
    content = models.TextField(
        verbose_name="Содержимое",
        blank=True,
        null=True,
        help_text='Введите статью.'
    )
    preview = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Превью статьи",
        help_text='Добавьте изображение.'
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        blank=True,
        null=True
    )
    published = models.BooleanField(
        verbose_name="Опубликована",
        blank=True
    )
    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите количество просмотров',
        default=0
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.title}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
