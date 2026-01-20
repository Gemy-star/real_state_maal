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
    Report,
    ChatbotQA,
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


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "is_active", "created_at")
    list_filter = ("is_active", "year")
    search_fields = ("year", "title", "description")
    ordering = ("-year",)
    list_editable = ("is_active",)


@admin.register(ChatbotQA)
class ChatbotQAAdmin(admin.ModelAdmin):
    list_display = ("question_preview", "category", "order", "is_active", "view_count", "created_at")
    list_filter = ("is_active", "category", "created_at")
    search_fields = ("question", "answer", "keywords", "category")
    ordering = ("order", "-created_at")
    list_editable = ("order", "is_active")
    readonly_fields = ("view_count", "created_at", "updated_at")

    def question_preview(self, obj):
        return obj.question[:50] + "..." if len(obj.question) > 50 else obj.question
    question_preview.short_description = "Question"
