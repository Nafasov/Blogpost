from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tags, )
    title = models.CharField(max_length=255)
    slug = models.SlugField(editable=True, )
    image = models.ImageField(upload_to='articles/', )
    content = RichTextField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/comment', null=True, blank=True)
    massage = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)







