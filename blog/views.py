from django.core.cache import cache
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Article
from config.settings import CACHE_ENABLED


class ArticleListView(ListView):
    model = Article

    @staticmethod
    def get_articles_from_cache():
        """Получает данные из кэша, если кэш пуст, получает данные из бд."""
        if not CACHE_ENABLED:
            return Article.objects.all()
        key = 'articles_list'
        articles = Article.get(key)
        if articles is not None:
            return articles
        articles = Article.objects.all()
        cache.set(key, articles)
        return articles


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'slug', 'content', 'preview', 'published')
    success_url = reverse_lazy('blog:articles_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'slug', 'content', 'preview', 'published')
    success_url = reverse_lazy('blog:articles_list')

    def get_success_url(self):
        return reverse('blog:articles_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles_list')

