from django.urls import path

from .view import article_list_api_view, article_detail_api_view


app_name = 'article_api'


urlpatterns = [
    path('list/', article_list_api_view, name='list'),
    path('detail/<int:pk>/', article_detail_api_view, name='detail')
]
