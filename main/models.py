# -*- coding: utf-8 -*-
from django.db import models
from django.templatetags.static import static

from .singleton_model import SingletonModel

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

    @property
    def image_url(self):
        # Check if the field is None (null) or an empty string
        if self.image and str(self.image).strip():
            return self.image.url
        # Return the default static file URL
        return static("assets/img/home_who.jpg")

    def __str__(self):
        return self.title


# Example usage
class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default="My Site")
    maintenance_mode = models.BooleanField(default=False)


class HomePageContent(SingletonModel):
    welcome_header = models.TextField(null=True, blank=True)
    welcome_background = models.ImageField(
        upload_to="backgrounds/", null=True, blank=True
    )
    welcome_btn_text = models.CharField(max_length=255, null=True, blank=True)
    home_first_paragrapgh = models.TextField(null=True, blank=True)
    first_paragrapgh_background = models.ImageField(
        upload_to="backgrounds/", null=True, blank=True
    )
    roaya_paragraph = models.TextField(null=True, blank=True)
    messages_paragraph = models.TextField(null=True, blank=True)
    goals_paragraph = models.TextField(null=True, blank=True)

    @property
    def background_url(self):
        # Check if the field is None (null) or an empty string
        if self.welcome_background and str(self.welcome_background).strip():
            return self.welcome_background.url
        # Return the default static file URL
        return static("assets/img/home_main.jpg")

    @property
    def first_paragrapgh_background_url(self):
        # Check if the field is None (null) or an empty string
        if (
            self.first_paragrapgh_background
            and str(self.first_paragrapgh_background).strip()
        ):
            return self.first_paragrapgh_background.url
        # Return the default static file URL
        return static("assets/img/home_who.jpg")


class RelationsPage(SingletonModel):
    first_paragraph_title = models.CharField(max_length=255, null=True, blank=True)
    first_paragraph = models.TextField(null=True, blank=True)
    second_paragraph_title = models.CharField(max_length=255, null=True, blank=True)
    second_paragraph = models.TextField(null=True, blank=True)
    first_paragrapgh_background = models.ImageField(
        upload_to="backgrounds/", null=True, blank=True
    )
    second_paragrapgh_background = models.ImageField(
        upload_to="backgrounds/", null=True, blank=True
    )

    @property
    def first_paragrapgh_background_url(self):
        # Check if the field is None (null) or an empty string
        if (
            self.first_paragrapgh_background
            and str(self.first_paragrapgh_background).strip()
        ):
            return self.first_paragrapgh_background.url
        # Return the default static file URL
        return static("assets/img/green.jpg")

    @property
    def second_paragrapgh_background_url(self):
        # Check if the field is None (null) or an empty string
        if (
            self.second_paragrapgh_background
            and str(self.second_paragrapgh_background).strip()
        ):
            return self.second_paragrapgh_background.url
        # Return the default static file URL
        return static("assets/img/home_1.jpg")


class WhoUsPage(SingletonModel):
    main_title = models.CharField(max_length=255, null=True, blank=True)
    main_subtitle = models.TextField(null=True, blank=True)
    main_background = models.ImageField(upload_to="backgrounds/", null=True, blank=True)

    @property
    def main_background_url(self):
        # Check if the field is None (null) or an empty string
        if self.main_background and str(self.main_background).strip():
            return self.main_background.url
        # Return the default static file URL
        return static("assets/img/home_1.jpg")
