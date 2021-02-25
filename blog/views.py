from django.shortcuts import render, get_object_or_404
from .models import Blog
from hitcount.views import HitCountDetailView


def blog(req):
    blog = Blog.objects
    return render(req, 'blog/blog.html', {'blog': blog})


def article(req, article_id):
    article = get_object_or_404(Blog, pk=article_id)
    return render(req, 'blog/article.html', {'article': article})


class PostDetailView(HitCountDetailView):
    model = Blog
    template_name = "blog/blog.html"
    count_hit = True
