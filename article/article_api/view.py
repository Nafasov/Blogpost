from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .serializers import ArticleSerializer, TagSerializer, CategorySerializer
from article.models import Article, Category, Tags


@api_view(['GET'])
def article_list_api_view(request, *args, **kwargs):
    articles = Article.objects.all().order_by('-id')
    tags = Tags.objects.all()
    categories = Category.objects.all()
    tags_serializer = TagSerializer(tags, many=True)
    categories_serializer = CategorySerializer(categories, many=True)
    article_serializer = ArticleSerializer(articles, many=True)
    context = {
        'categories_serializer': categories_serializer,
        'article_serializer': article_serializer,
    }
    return Response(article_serializer.data)


@api_view(['GET'])
def article_detail_api_view(request, *args, **kwargs):
    article = get_object_or_404(Article, pk=kwargs['pk'])
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
