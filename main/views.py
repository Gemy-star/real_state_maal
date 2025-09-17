# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, TemplateView
)

from .forms import ContactForm, JobRequestForm, ProjectRequestForm
from .models import (
    Contact, HomePageContent, JobRequest, News,
    ProjectRequest, RelationsPage, WhoUsPage
)


# -------------------- PUBLIC VIEWS --------------------

class HomePageView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = HomePageContent.get_instance()
        context["news"] = News.objects.all().order_by("-id")
        return context


def home_page_view(request):
    return redirect("home-page")


class PrivacyPageView(TemplateView):
    template_name = "main/privacy.html"


class NewsPageView(ListView):
    template_name = "main/news.html"
    model = News
    context_object_name = "news"
    paginate_by = 10
    ordering = ["-id"]


class SoonPageView(TemplateView):
    template_name = "main/soon.html"

class ThimarReportsPageView(TemplateView):
    template_name="main/reports_pdf.html"
    
class AboutPageView(TemplateView):
    template_name = "main/about.html"


class ReportsPageView(TemplateView):
    template_name = "main/reports.html"


class MaalPageView(TemplateView):
    template_name = "main/maaal.html"


class WhoUsPageView(TemplateView):
    template_name = "main/who_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = WhoUsPage.get_instance()
        context["news"] = News.objects.all().order_by("-id")
        return context


class ContactPageView(CreateView):
    template_name = "main/contact.html"
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy("contact-page")

    def get_context_data(self, **kwargs) -> dict:
        ctx = super().get_context_data(**kwargs)
        ctx["news"] = News.objects.all().order_by("-id")
        return ctx

    def form_valid(self, form):
        messages.success(self.request, _("تم إرسال رسالتك بنجاح!"))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _("حدث خطأ أثناء إرسال رسالتك. يرجى المحاولة مرة أخرى."))
        return super().form_invalid(form)


class ServicesPageView(CreateView):
    template_name = "main/services.html"
    form_class = ProjectRequestForm
    model = ProjectRequest
    success_url = reverse_lazy("services-page")

    def form_valid(self, form):
        messages.success(self.request, _("تم إرسال طلبك بنجاح! سنتواصل معك قريبًا."))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _("حدث خطأ أثناء إرسال طلبك. يرجى المحاولة مرة أخرى."))
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home_content"] = WhoUsPage.get_instance()
        context["news"] = News.objects.all().order_by("-id")
        context["content"] = RelationsPage.get_instance()
        return context


# -------------------- DASHBOARD VIEWS --------------------

class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "main/dashboard/contact_list.html"
    context_object_name = "contacts"
    login_url = reverse_lazy("login")

    def get_queryset(self):
        messages.success(self.request, _("تم تحميل قائمة جهات الاتصال بنجاح."))
        return super().get_queryset().order_by("-id")


class JobRequestListView(LoginRequiredMixin, ListView):
    model = JobRequest
    template_name = "main/dashboard/jobrequest_list.html"
    context_object_name = "jobrequests"
    login_url = reverse_lazy("login")

    def get_queryset(self):
        messages.success(self.request, _("تم تحميل قائمة طلبات الوظائف بنجاح."))
        return super().get_queryset().order_by("-id")


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "main/dashboard/contact_detail.html"
    login_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        messages.info(self.request, _("عرض تفاصيل جهة الاتصال: %(name)s.") % {
            "name": self.get_object().name
        })
        return super().get(request, *args, **kwargs)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "main/dashboard/_contact_delete.html"
    success_url = reverse_lazy("contact-list")
    login_url = reverse_lazy("login")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _("تم حذف جهة الاتصال: %(name)s بنجاح.") % {
            "name": self.get_object().name
        })
        return super().delete(request, *args, **kwargs)


class JobRequestDetailView(LoginRequiredMixin, DetailView):
    model = JobRequest
    template_name = "main/dashboard/jobrequest_detail.html"
    login_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        messages.info(self.request, _("عرض تفاصيل طلب الوظيفة: %(name)s.") % {
            "name": self.get_object().name
        })
        return super().get(request, *args, **kwargs)


class JobRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = JobRequest
    template_name = "main/dashboard/_job_request_delete.html"
    success_url = reverse_lazy("jobrequest-list")
    login_url = reverse_lazy("login")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _("تم حذف طلب الوظيفة: %(name)s بنجاح.") % {
            "name": self.get_object().name
        })
        return super().delete(request, *args, **kwargs)


# -------------------- AUTH --------------------

class ThimarLoginView(LoginView):
    template_name = "main/dashboard/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy("contact-list")

    def form_invalid(self, form):
        messages.error(self.request, _("فشل تسجيل الدخول. يرجى التحقق من اسم المستخدم وكلمة المرور."))
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, _("تم تسجيل الدخول بنجاح."))
        return super().form_valid(form)
