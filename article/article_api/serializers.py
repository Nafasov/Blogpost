
from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'tags', 'category', 'image', 'modified_date', 'created_date']
