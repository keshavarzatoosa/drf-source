from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.shortcuts import render
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response


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
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)
    # This parameter is equale "pk" as default if you don't write it
    # lookup_field = "pk"
    # If you want to put this field equale to "slug"
    # lookup_field = "slug"


class UserList(ListCreateAPIView):
    # queryset = User.objects.all()
    def get_queryset(self):
        # print username
        # print(self.request.user)
        # print token
        # print(self.request.auth)
        # delete an extistin Token
        # self.request.auth.delete()
        return User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsSuperUser,)
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsSuperUserOrStaffReadOnly,)
    # authentication_classes = (SessionAuthentication,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsSuperUser,)
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsSuperUserOrStaffReadOnly,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)

#     # def get(self, request):
#     #     return Response({"mehtod": "get"})

#     # def post(self, request):
#     #     return Response({"mehtod": "post"})

#     # def put(self, request):
#     #     return Response({"mehtod": "put"})

#     def delete(self, request):
#         request.auth.delete()
#         # return Response({"msg": "Token revoked"}, status=201)
#         # status = 204 can not have any content
#         return Response(status=204)