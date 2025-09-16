# -*- coding: utf-8 -*-
from django.db import models
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _  # ✅ for translations
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

from .singleton_model import SingletonModel


class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone"), max_length=50)
    subject = models.CharField(_("Subject"), max_length=100)
    message = models.TextField(_("Message"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name


class ProjectRequest(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone"), max_length=50)
    description = models.TextField(_("Description"))
    project_file = models.ImageField(
        _("Project File"), null=True, blank=True, upload_to="reports/"
    )

    project_file_thumb = ImageSpecField(
        source="project_file",
        processors=[ResizeToFill(300, 200)],
        format="JPEG",
        options={"quality": 80},
    )
    project_file_large = ImageSpecField(
        source="project_file",
        processors=[ResizeToFit(1200, 800)],
        format="JPEG",
        options={"quality": 90},
    )

    class Meta:
        verbose_name = _("Project Request")
        verbose_name_plural = _("Project Requests")

    def __str__(self):
        return self.name


class JobRequest(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    field = models.CharField(_("Field"), max_length=50)
    cv = models.FileField(_("CV"), null=True, blank=True, upload_to="CV/")

    class Meta:
        verbose_name = _("Job Request")
        verbose_name_plural = _("Job Requests")

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.TextField(_("Title"))
    content = models.TextField(_("Content"))
    image = models.ImageField(_("Image"), null=True, blank=True, upload_to="news/")

    image_thumb = ImageSpecField(
        source="image",
        processors=[ResizeToFill(400, 250)],
        format="JPEG",
        options={"quality": 85},
    )
    image_large = ImageSpecField(
        source="image",
        processors=[ResizeToFit(1280, 720)],
        format="JPEG",
        options={"quality": 90},
    )

    @property
    def image_url(self):
        return self.image.url if self.image else static("assets/img/home_who.jpg")

    @property
    def image_thumb_url(self):
        return self.image_thumb.url if self.image else static("assets/img/home_who.jpg")

    @property
    def image_large_url(self):
        return self.image_large.url if self.image else static("assets/img/home_who.jpg")

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __str__(self):
        return self.title


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(_("Site Name"), max_length=255, default="My Site")
    maintenance_mode = models.BooleanField(_("Maintenance Mode"), default=False)

    class Meta:
        verbose_name = _("Site Configuration")
        verbose_name_plural = _("Site Configuration")


class HomePageContent(SingletonModel):
    welcome_header = models.TextField(_("Welcome Header"), null=True, blank=True)
    welcome_background = models.ImageField(
        _("Welcome Background"), upload_to="backgrounds/", null=True, blank=True
    )
    welcome_btn_text = models.CharField(
        _("Welcome Button Text"), max_length=255, null=True, blank=True
    )
    home_first_paragrapgh = models.TextField(
        _("First Paragraph"), null=True, blank=True
    )
    first_paragrapgh_background = models.ImageField(
        _("First Paragraph Background"), upload_to="backgrounds/", null=True, blank=True
    )
    roaya_paragraph = models.TextField(_("Vision Paragraph"), null=True, blank=True)
    messages_paragraph = models.TextField(_("Messages Paragraph"), null=True, blank=True)
    goals_paragraph = models.TextField(_("Goals Paragraph"), null=True, blank=True)

    welcome_background_large = ImageSpecField(
        source="welcome_background",
        processors=[ResizeToFit(1600, 900)],
        format="JPEG",
        options={"quality": 90},
    )
    first_paragrapgh_background_large = ImageSpecField(
        source="first_paragrapgh_background",
        processors=[ResizeToFit(1600, 900)],
        format="JPEG",
        options={"quality": 90},
    )

    @property
    def background_url(self):
        return self.welcome_background_large.url if self.welcome_background else static(
            "assets/img/home_main.jpg"
        )

    @property
    def first_paragrapgh_background_url(self):
        return (
            self.first_paragrapgh_background_large.url
            if self.first_paragrapgh_background
            else static("assets/img/home_who.jpg")
        )

    class Meta:
        verbose_name = _("Home Page Content")
        verbose_name_plural = _("Home Page Content")


class RelationsPage(SingletonModel):
    first_paragraph_title = models.CharField(
        _("First Paragraph Title"), max_length=255, null=True, blank=True
    )
    first_paragraph = models.TextField(_("First Paragraph"), null=True, blank=True)
    second_paragraph_title = models.CharField(
        _("Second Paragraph Title"), max_length=255, null=True, blank=True
    )
    second_paragraph = models.TextField(_("Second Paragraph"), null=True, blank=True)
    first_paragrapgh_background = models.ImageField(
        _("First Paragraph Background"), upload_to="backgrounds/", null=True, blank=True
    )
    second_paragrapgh_background = models.ImageField(
        _("Second Paragraph Background"), upload_to="backgrounds/", null=True, blank=True
    )

    first_paragrapgh_background_large = ImageSpecField(
        source="first_paragrapgh_background",
        processors=[ResizeToFit(1600, 900)],
        format="JPEG",
        options={"quality": 90},
    )
    second_paragrapgh_background_large = ImageSpecField(
        source="second_paragrapgh_background",
        processors=[ResizeToFit(1600, 900)],
        format="JPEG",
        options={"quality": 90},
    )

    @property
    def first_paragrapgh_background_url(self):
        return (
            self.first_paragrapgh_background_large.url
            if self.first_paragrapgh_background
            else static("assets/img/green.jpg")
        )

    @property
    def second_paragrapgh_background_url(self):
        return (
            self.second_paragrapgh_background_large.url
            if self.second_paragrapgh_background
            else static("assets/img/home_1.jpg")
        )

    class Meta:
        verbose_name = _("Relations Page")
        verbose_name_plural = _("Relations Pages")


class WhoUsPage(SingletonModel):
    main_title = models.CharField(_("Main Title"), max_length=255, null=True, blank=True)
    main_subtitle = models.TextField(_("Main Subtitle"), null=True, blank=True)
    main_background = models.ImageField(
        _("Main Background"), upload_to="backgrounds/", null=True, blank=True
    )

    main_background_large = ImageSpecField(
        source="main_background",
        processors=[ResizeToFit(1600, 900)],
        format="JPEG",
        options={"quality": 90},
    )

    @property
    def main_background_url(self):
        return self.main_background_large.url if self.main_background else static(
            "assets/img/home_1.jpg"
        )

    class Meta:
        verbose_name = _("Who Us Page")
        verbose_name_plural = _("Who Us Pages")
