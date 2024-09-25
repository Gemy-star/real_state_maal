# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class ProjectRequest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    description = models.TextField()
    project_file = models.ImageField(null=True, blank=True, upload_to="reports/")

    def __str__(self):
        return self.name


class JobRequest(models.Model):
    name = models.CharField(max_length=50)
    field = models.CharField(max_length=50)
    cv = models.FileField(null=True, blank=True, upload_to="CV/")

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="news/")

    def __str__(self):
        return self.title
