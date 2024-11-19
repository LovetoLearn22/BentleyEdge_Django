from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()

    # Apply filters based on query parameters
    topic = request.GET.get('topic')
    if topic:
        articles = articles.filter(topic=topic)

    author = request.GET.get('author')
    if author:
        articles = articles.filter(author__icontains=author)

    community = request.GET.get('community')
    if community:
        articles = articles.filter(community=community)

    date = request.GET.get('date')
    if date:
        articles = articles.filter(created_at__date=date)

    return render(request, 'edge/article_list.html', {'articles': articles})
