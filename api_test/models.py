
# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name


class TestProject(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    is_del = models.IntegerField(default=0)

class TestSuite(models.Model):
    suite_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    variables = models.CharField(max_length=500, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    project_id = models.ForeignKey(TestProject, blank=True, null=True, on_delete=models.CASCADE)
    is_del = models.IntegerField(default=0)

class TestCase(models.Model):
    case_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    variables = models.CharField(max_length=500, blank=True, null=True)
    request = models.TextField()
    extract = models.CharField(max_length=500, blank=True, null=True)
    validate = models.CharField(max_length=500)
    suite_id = models.ForeignKey(TestSuite, blank=True, null=True, on_delete=models.CASCADE)
    is_del = models.IntegerField(default=0)



