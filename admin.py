from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'topic', 'community', 'created_at')
    list_filter = ('topic', 'community', 'created_at')
    search_fields = ('title', 'author')
