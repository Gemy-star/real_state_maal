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
]
