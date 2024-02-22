from django.urls import path

from .views import (
    article_view,
    article_detail_view,
    element_view,
    category_view
)

app_name = 'article'


urlpatterns = [
    path('list/', article_view, name='article_list'),
    path('detail/<slug:slug>/', article_detail_view, name='article_detail'),
    path('element/daren/', element_view, name='element_l'),
    path('category/list/', category_view, name='category')

]