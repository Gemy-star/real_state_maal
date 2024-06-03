from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "main/home.html"


class SoonPageView(TemplateView):
    template_name = "main/soon.html"


class AboutPageView(TemplateView):
    template_name = "main/about.html"
