from rest_framework.generics import ListAPIView, ListCreateAPIView
from django.shortcuts import render
from blog.models import Article
from .serializers import ArticleSerializer


# class ArticleList(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
