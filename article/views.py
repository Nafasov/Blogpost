from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


from .models import Article, Tags, Category, Comment
from .forms import CommentForm


def article_view(request):
    tags = Tags.objects.order_by("-id")
    categories = Category.objects.order_by("-id")
    articles = Article.objects.order_by("-id")
    q = request.GET.get('q')
    if q:
        q = Q(title__icontains=q)
        articles = Article.objects.filter(q).order_by('-id')
    paginator = Paginator(articles, 8)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'object_list': articles,
        'tags': tags,
        'categories': categories
    }
    return render(request, 'article/archive.html', context)


def article_detail_view(request, slug, *args, **kwargs):
    form = CommentForm()
    article = Article.objects.get(slug=slug)
    tags = Tags.objects.order_by("-id")
    categories = Category.objects.order_by("-id")
    comments = Comment.objects.filter(article_id=article.id, top_level_comment_id__isnull=True)
    cid = request.GET.get('cid')
    if request.method == "POST":
        comment = CommentForm(request.POST, request.FILES)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.article = article
            comment.parent_id = cid
            comment.save()
            messages.success(request, 'Comment sent successfully!')
            return redirect(".")

    next = Article.objects.filter(pk__gt=article.pk).order_by('pk').first()
    previous = Article.objects.filter(pk__lt=article.pk).order_by('-pk').first()

    context = {
        'object': article,
        'tags': tags,
        'categories': categories,
        'form': form,
        'next': next,
        'previous': previous,
        'comments': comments,
    }
    return render(request, 'article/single-blog.html', context)


def category_view(request):
    tags = Tags.objects.order_by("-id")
    categories = Category.objects.order_by("-id")
    articles = Article.objects.all()
    category = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if q:
        q = Q(title__icontains=q)
        articles = articles.filter(q).order_by('-id')
    if category:
        articles = articles.filter(category__title__exact=category)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    paginator = Paginator(articles, 8)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
        'objects': articles,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'article/category.html', context)


def element_view(requests):
    context = {

    }
    return render(requests, 'article/elements.html', context)

