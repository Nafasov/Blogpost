from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleSerializer, TagSerializer, CategorySerializer, CommentSerializer
from article.models import Article, Category, Tags, Comment, Content


@api_view(['GET'])
def article_list_api_view(request, *args, **kwargs):
    tags = Tags.objects.all()
    categories = Category.objects.all()
    articles = Article.objects.all().order_by('-id')
    q = request.GET.get('q')
    if q:
        q = Q(title__icontains=q)
        articles = articles.filter(q).order_by('-id')
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    tags_serializer = TagSerializer(tags, many=True)
    categories_serializer = CategorySerializer(categories, many=True)
    article_serializer = ArticleSerializer(articles, many=True)
    context = {
        'article_serializer': article_serializer.data,
        'categories_serializer': categories_serializer.data,
        'tags_serializer': tags_serializer.data
    }
    return Response(context)


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'massage': openapi.Schema(type=openapi.TYPE_STRING),
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'image': openapi.Schema(type=openapi.TYPE_FILE),

        },
        required=['massage', 'name', 'image']
    ),
    responses={
        200: 'Success',
        400: 'Bad Request',
    },
    operation_id='custom_operation_id'
)
@api_view(['GET', 'POST'])
def article_detail_api_view(request, *args, **kwargs):
    article = get_object_or_404(Article, pk=kwargs['pk'])
    if request.method == 'POST':
        cid = request.POST.get('cid')
        context = {
            'article_id': kwargs['pk'],
            'cid': cid,
        }
        comment = CommentSerializer(data=request.data, context=context)
        comment.is_valid(raise_exception=True)
        comment.save()
        context = {
            'comment': comment.data
        }
        return Response(context)
    article_serializer = ArticleSerializer(article)
    context = {
        'article_serializer': article_serializer.data
    }
    return Response(context)
