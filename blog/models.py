from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pub.models import params_get
from pub.config.pub_definitions import ParameterType


class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Person(models.Model):

    def _select_status():
        return params_get(ParameterType.PT_ActivePassive.value)

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    status = models.CharField(choices=_select_status, max_length=12)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Bank(models.Model):

    def _select_bank_type():
        return params_get(ParameterType.PT_BankType.value)

    def _select_status():
        return params_get(ParameterType.PT_ActivePassive.value)

    name = models.CharField(max_length=250)
    manager_name = models.CharField(max_length=250)
    type = models.CharField(choices=_select_bank_type, max_length=12)
    status = models.CharField(choices=_select_status, max_length=12)
    address = models.CharField(max_length=250)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
