from django import template

from article.models import Article

register = template.Library()


@register.simple_tag
def footer_article():
    return Article.objects.order_by("-id")[:3]
