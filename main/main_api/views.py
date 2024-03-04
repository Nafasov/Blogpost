from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from article.models import Article, Tags, Category
from article.article_api.serializers import CategorySerializer, TagSerializer, ArticleSerializer
from main.main_api.serializers import ContactSerializer


@api_view(['GET'])
def home_api_view(request):
    articles = Article.objects.order_by('id')[3:9:]
    tags = Tags.objects.all()
    categories = Category.objects.all()
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
    articles_serializer = ArticleSerializer(articles, many=True)
    tags_serializer = TagSerializer(tags, many=True)
    categories_serializer = CategorySerializer(categories, many=True)
    context = {
        'articles': articles_serializer.data,
        'tags': tags_serializer.data,
        'categories': categories_serializer.data
    }
    return Response(context)


@api_view(['POST'])
def contact_api_view(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        context = {
            'success': True,
            'message': 'Contact successfully sent!'
        }
        return Response(context)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
