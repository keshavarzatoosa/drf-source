from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User


# get all objects
# class ArticleList(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# get all objects and create an object
class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# get an object
# class ArticleDetail(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# delete an object
# class ArticleDetail(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# get and delete an object
# class ArticleDetail(RetrieveDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# post an object
# class ArticleDetail(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# get and post an object
# class ArticleDetail(RetrieveUpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# get and post and delete an object
class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # This parameter is equale "pk" as default if you don't write it
    # lookup_field = "pk"
    # If you want to put this field equale to "slug"
    # lookup_field = "slug"



class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
