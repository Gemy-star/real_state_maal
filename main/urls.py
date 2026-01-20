# -*- coding: utf-8 -*-
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

urlpatterns = [
    path("main", HomePageView.as_view(), name="home-page"),
    path("", home_page_view, name="main-page"),
    # path("", SoonPageView.as_view(), name="soon-page"),
    path("about/", AboutPageView.as_view(), name="about-page"),
    path("reports/", ReportsPageView.as_view(), name="reports-page"),
    path("maaal/", MaalPageView.as_view(), name="maal-page"),
    path("who-us/", WhoUsPageView.as_view(), name="who-page"),
    path("services/", ServicesPageView.as_view(), name="services-page"),
    path("contact/", ContactPageView.as_view(), name="contact-page"),
    path("news/", NewsPageView.as_view(), name="news-page"),
    path("privacy/", PrivacyPageView.as_view(), name="privacy-page"),
    path("contacts/", ContactListView.as_view(), name="contact-list"),
    path("jobrequests/", JobRequestListView.as_view(), name="jobrequest-list"),
    path(
        "translations/",
        TranslationManagementView.as_view(),
        name="translation-management",
    ),
    path("reports-manage/", ReportListView.as_view(), name="report-list"),
    path("reports-manage/add/", ReportCreateView.as_view(), name="report-add"),
    path("reports-manage/<int:pk>/", ReportDetailView.as_view(), name="report-detail"),
    path(
        "reports-manage/<int:pk>/delete/",
        ReportDeleteView.as_view(),
        name="report-delete",
    ),
    path("report/thimar/", ThimarReportsPageView.as_view(), name="report-thimar"),
    path("contact/<int:pk>/", ContactDetailView.as_view(), name="contact-detail"),
    path(
        "contact/<int:pk>/delete/", ContactDeleteView.as_view(), name="contact-delete"
    ),
    path(
        "jobrequest/<int:pk>/", JobRequestDetailView.as_view(), name="jobrequest-detail"
    ),
    path(
        "jobrequest/<int:pk>/delete/",
        JobRequestDeleteView.as_view(),
        name="jobrequest-delete",
    ),
    path("login/", ThimarLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("settings/", SiteSettingsView.as_view(), name="site-settings"),
    path(
        "settings/update/",
        SiteSettingsUpdateView.as_view(),
        name="site-settings-update",
    ),    # Chatbot management
    path("chatbot/", ChatbotListView.as_view(), name="chatbot-list"),
    path("chatbot/add/", ChatbotCreateView.as_view(), name="chatbot-add"),
    path("chatbot/<int:pk>/", ChatbotDetailView.as_view(), name="chatbot-detail"),
    path(
        "chatbot/<int:pk>/update/", ChatbotUpdateView.as_view(), name="chatbot-update"
    ),
    path(
        "chatbot/<int:pk>/delete/", ChatbotDeleteView.as_view(), name="chatbot-delete"
    ),
    # Chatbot API
    path("api/chatbot/search/", ChatbotSearchView.as_view(), name="chatbot-search"),
    path("api/chatbot/all/", ChatbotGetAllView.as_view(), name="chatbot-all"),]
