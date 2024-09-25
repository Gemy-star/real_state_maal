# -*- coding: utf-8 -*-
from django.urls import path

from .views import (AboutPageView, ContactPageView, HomePageView, NewsPageView,
                    PrivacyPageView, ReportsPageView, ServicesPageView,
                    WhoUsPageView)

urlpatterns = [
    path("main", HomePageView.as_view(), name="home-page"),
    path("", HomePageView.as_view(), name="main-page"),
    # path("", SoonPageView.as_view(), name="soon-page"),
    path("about", AboutPageView.as_view(), name="about-page"),
    path("reports", ReportsPageView.as_view(), name="reports-page"),
    path("who-us", WhoUsPageView.as_view(), name="who-page"),
    path("services", ServicesPageView.as_view(), name="services-page"),
    path("contact", ContactPageView.as_view(), name="contact-page"),
    path("news", NewsPageView.as_view(), name="news-page"),
    path("privacy", PrivacyPageView.as_view(), name="privacy-page"),
]
