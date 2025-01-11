from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # exclude = ['created', 'updated']
        # fields = ['title', 'slug', 'author', 'content', 'publish', 'staus']
        fields = "__all__"