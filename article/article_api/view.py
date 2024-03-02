from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleSerializer
from article.models import Article


@api_view(['GET'])
def article_list_api_view(request,*args,**kwargs):
    articles = Article.objects.all().order_by('-id')
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_detail_api_view(request, *args, **kwargs):
    article = get_object_or_404(Article, pk=kwargs['pk'])
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
