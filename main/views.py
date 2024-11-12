# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import ContactForm, JobRequestForm, ProjectRequestForm
from .models import Contact, JobRequest, News, ProjectRequest

# Create your views here.


class HomePageView(TemplateView):
    template_name = "main/home.html"


def home_page_view(request):
    return redirect("home-page")


class PrivacyPageView(TemplateView):
    template_name = "main/privacy.html"


class NewsPageView(CreateView):
    template_name = "main/news.html"
    form_class = JobRequestForm
    model = JobRequest
    success_url = reverse_lazy("news-page")


class SoonPageView(TemplateView):
    template_name = "main/soon.html"


class AboutPageView(TemplateView):
    template_name = "main/about.html"


class ReportsPageView(TemplateView):
    template_name = "main/reports.html"


class WhoUsPageView(TemplateView):
    template_name = "main/who_us.html"


class ContactPageView(CreateView):
    def get_context_data(self, **kwargs) -> dict:
        ctx = super().get_context_data(**kwargs)
        news = News.objects.all().order_by("-pk")
        ctx.update({"news": news})
        return ctx

    template_name = "main/contact.html"
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy("contact-page")


class ServicesPageView(CreateView):
    template_name = "main/services.html"
    form_class = ProjectRequestForm
    model = ProjectRequest
    success_url = reverse_lazy("project-page")
