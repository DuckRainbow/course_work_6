from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog', ArticleListView.as_view(), name='articles_list'),
    path('blog/<int:pk>/', ArticleDetailView.as_view(), name='articles_detail'),
    path('blog/create', ArticleCreateView.as_view(), name='articles_create'),
    path('blog/<int:pk>/update/', ArticleUpdateView.as_view(), name='articles_update'),
    path('blog/<int:pk>/delete/', ArticleDeleteView.as_view(), name='articles_delete')
]

