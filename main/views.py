# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView)

from .forms import ContactForm, JobRequestForm, ProjectRequestForm
from .models import (Contact, HomePageContent, JobRequest, News,
                     ProjectRequest, RelationsPage, WhoUsPage)


class HomePageView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the default context
        context = super().get_context_data(**kwargs)

        # Add extra context data
        context["content"] = HomePageContent.get_instance()
        return context


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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the default context
        context = super().get_context_data(**kwargs)

        # Add extra context data
        context["content"] = WhoUsPage.get_instance()
        context["news"] = News.objects.all()
        return context


class ContactPageView(CreateView):
    template_name = "main/contact.html"
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy("contact-page")

    def get_context_data(self, **kwargs) -> dict:
        ctx = super().get_context_data(**kwargs)
        news = News.objects.all().order_by("-pk")
        ctx.update({"news": news})
        return ctx

    def form_valid(self, form):
        """Called when the form is valid."""
        messages.success(self.request, "تم إرسال رسالتك بنجاح!")
        return super().form_valid(form)

    def form_invalid(self, form):
        """Called when the form is invalid."""
        messages.error(
            self.request, "حدث خطأ أثناء إرسال رسالتك. يرجى المحاولة مرة أخرى."
        )
        return super().form_invalid(form)


class ServicesPageView(CreateView):
    template_name = "main/services.html"
    form_class = ProjectRequestForm
    model = ProjectRequest
    success_url = reverse_lazy("project-page")

    def form_valid(self, form):
        """Called when the form is valid."""
        messages.success(self.request, "تم إرسال طلبك بنجاح! سنتواصل معك قريبًا.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """Called when the form is invalid."""
        messages.error(
            self.request, "حدث خطأ أثناء إرسال طلبك. يرجى المحاولة مرة أخرى."
        )
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the default context
        context = super().get_context_data(**kwargs)

        # Add extra context data
        context["content"] = RelationsPage.get_instance()
        return context


# Contact List View
class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "main/dashboard/contact_list.html"
    context_object_name = "contacts"
    login_url = reverse_lazy("login")  # Redirect if not logged in

    def get_queryset(self):
        messages.success(self.request, "تم تحميل قائمة جهات الاتصال بنجاح.")
        return super().get_queryset()


# JobRequest List View
class JobRequestListView(LoginRequiredMixin, ListView):
    model = JobRequest
    template_name = "main/dashboard/jobrequest_list.html"
    context_object_name = "jobrequests"
    login_url = reverse_lazy("login")  # Redirect if not logged in

    def get_queryset(self):
        messages.success(self.request, "تم تحميل قائمة طلبات الوظائف بنجاح.")
        return super().get_queryset()


# Contact Detail View
class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "main/dashboard/contact_detail.html"
    login_url = reverse_lazy("login")  # Redirect if not logged in

    def get(self, request, *args, **kwargs):
        messages.info(
            self.request, f"عرض تفاصيل جهة الاتصال: {self.get_object().name}."
        )
        return super().get(request, *args, **kwargs)


# Contact Delete View
class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "main/dashboard/_contact_delete.html"
    success_url = reverse_lazy("contact-list")
    login_url = reverse_lazy("login")  # Redirect if not logged in

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, f"تم حذف جهة الاتصال: {self.get_object().name} بنجاح."
        )
        return super().delete(request, *args, **kwargs)


# JobRequest Detail View
class JobRequestDetailView(LoginRequiredMixin, DetailView):
    model = JobRequest
    template_name = "main/dashboard/jobrequest_detail.html"
    login_url = reverse_lazy("login")  # Redirect if not logged in

    def get(self, request, *args, **kwargs):
        messages.info(
            self.request, f"عرض تفاصيل طلب الوظيفة: {self.get_object().name}."
        )
        return super().get(request, *args, **kwargs)


# JobRequest Delete View
class JobRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = JobRequest
    template_name = "main/dashboard/_job_request_delete.html"
    success_url = reverse_lazy("jobrequest-list")
    login_url = reverse_lazy("login")  # Redirect if not logged in

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, f"تم حذف طلب الوظيفة: {self.get_object().name} بنجاح."
        )
        return super().delete(request, *args, **kwargs)


# Custom Login View
class ThimarLoginView(LoginView):
    template_name = "main/dashboard/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy("contact-list")

    def form_invalid(self, form):
        messages.error(
            self.request, "فشل تسجيل الدخول. يرجى التحقق من اسم المستخدم وكلمة المرور."
        )
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "تم تسجيل الدخول بنجاح.")
        return super().form_valid(form)
