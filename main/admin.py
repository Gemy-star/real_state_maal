# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import (
    Contact,
    ProjectRequest,
    JobRequest,
    News,
    SiteConfiguration,
    HomePageContent,
    RelationsPage,
    WhoUsPage,
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "subject")
    search_fields = ("name", "email", "phone", "subject", "message")
    ordering = ("-id",)


@admin.register(ProjectRequest)
class ProjectRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email", "phone", "description")
    ordering = ("-id",)


@admin.register(JobRequest)
class JobRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "field")
    search_fields = ("name", "field")
    ordering = ("-id",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "image")
    search_fields = ("title", "content")
    ordering = ("-id",)


# Singleton Models → only allow editing the single instance
@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteConfiguration.objects.exists()


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not HomePageContent.objects.exists()


@admin.register(RelationsPage)
class RelationsPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not RelationsPage.objects.exists()


@admin.register(WhoUsPage)
class WhoUsPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not WhoUsPage.objects.exists()
