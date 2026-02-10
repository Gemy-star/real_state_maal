# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
from django.http import JsonResponse

from .forms import ContactForm, JobRequestForm, ProjectRequestForm
from .models import (
    Contact,
    HomePageContent,
    JobRequest,
    News,
    ProjectRequest,
    RelationsPage,
    WhoUsPage,
    Report,
    ChatbotQA,
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
    template_name = "main/reports_pdf.html"


class AboutPageView(TemplateView):
    template_name = "main/about.html"


class ReportsPageView(ListView):
    template_name = "main/reports.html"
    model = Report
    context_object_name = "reports"

    def get_queryset(self):
        return Report.objects.filter(is_active=True).order_by("-year")


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
        messages.error(
            self.request, _("حدث خطأ أثناء إرسال رسالتك. يرجى المحاولة مرة أخرى.")
        )
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
        messages.error(
            self.request, _("حدث خطأ أثناء إرسال طلبك. يرجى المحاولة مرة أخرى.")
        )
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
        messages.info(
            self.request,
            _("عرض تفاصيل جهة الاتصال: %(name)s.") % {"name": self.get_object().name},
        )
        return super().get(request, *args, **kwargs)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "main/dashboard/_contact_delete.html"
    success_url = reverse_lazy("contact-list")
    login_url = reverse_lazy("login")

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            _("تم حذف جهة الاتصال: %(name)s بنجاح.") % {"name": self.get_object().name},
        )
        return super().delete(request, *args, **kwargs)


class JobRequestDetailView(LoginRequiredMixin, DetailView):
    model = JobRequest
    template_name = "main/dashboard/jobrequest_detail.html"
    login_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        messages.info(
            self.request,
            _("عرض تفاصيل طلب الوظيفة: %(name)s.") % {"name": self.get_object().name},
        )
        return super().get(request, *args, **kwargs)


class JobRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = JobRequest
    template_name = "main/dashboard/_job_request_delete.html"
    success_url = reverse_lazy("jobrequest-list")
    login_url = reverse_lazy("login")

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            _("تم حذف طلب الوظيفة: %(name)s بنجاح.") % {"name": self.get_object().name},
        )
        return super().delete(request, *args, **kwargs)


# -------------------- AUTH --------------------


class ThimarLoginView(LoginView):
    template_name = "main/dashboard/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy("contact-list")

    def form_invalid(self, form):
        messages.error(
            self.request,
            _("فشل تسجيل الدخول. يرجى التحقق من اسم المستخدم وكلمة المرور."),
        )
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, _("تم تسجيل الدخول بنجاح."))
        return super().form_valid(form)


# -------------------- TRANSLATION MANAGEMENT --------------------


class TranslationManagementView(LoginRequiredMixin, TemplateView):
    template_name = "main/dashboard/translation_management.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("إدارة الترجمة")

        # Get available languages
        from django.conf import settings

        context["languages"] = settings.LANGUAGES

        # Get locale path info
        import os

        locale_path = settings.LOCALE_PATHS[0] if settings.LOCALE_PATHS else None
        context["locale_path"] = locale_path

        # Check if .po files exist for each language
        po_files_status = {}
        if locale_path:
            for lang_code, lang_name in settings.LANGUAGES:
                po_file_path = os.path.join(
                    locale_path, lang_code, "LC_MESSAGES", "django.po"
                )
                po_files_status[lang_code] = {
                    "name": lang_name,
                    "exists": os.path.exists(po_file_path),
                    "path": po_file_path if os.path.exists(po_file_path) else None,
                }

        context["po_files_status"] = po_files_status

        return context


# -------------------- SITE SETTINGS --------------------


class SiteSettingsView(LoginRequiredMixin, TemplateView):
    template_name = "main/dashboard/site_settings.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("إعدادات الموقع")

        # Get constance config
        from django.conf import settings
        from constance import config

        # Build settings list with current values
        settings_list = []
        for key, (default, help_text) in settings.CONSTANCE_CONFIG.items():
            settings_list.append(
                {
                    "key": key,
                    "value": getattr(config, key),
                    "default": default,
                    "help_text": help_text,
                }
            )

        context["settings_list"] = settings_list
        return context


class SiteSettingsUpdateView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        from constance import config
        from django.conf import settings as django_settings

        key = request.POST.get("key")
        value = request.POST.get("value")

        if key and key in django_settings.CONSTANCE_CONFIG:
            setattr(config, key, value)
            messages.success(request, _("تم تحديث الإعداد بنجاح."))
            return JsonResponse(
                {"success": True, "message": _("تم تحديث الإعداد بنجاح.")}
            )

        messages.error(request, _("حدث خطأ أثناء تحديث الإعداد."))
        return JsonResponse(
            {"success": False, "message": _("حدث خطأ أثناء تحديث الإعداد.")}, status=400
        )


# -------------------- REPORTS MANAGEMENT --------------------


class ReportListView(LoginRequiredMixin, ListView):
    """Dashboard view to list all reports"""

    template_name = "main/dashboard/report_list.html"
    model = Report
    context_object_name = "reports"
    login_url = reverse_lazy("login")
    paginate_by = 20

    def get_queryset(self):
        return Report.objects.all().order_by("-year")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_reports_count"] = Report.objects.filter(is_active=True).count()
        return context


class ReportCreateView(LoginRequiredMixin, CreateView):
    """Dashboard view to create a new report"""

    template_name = "main/dashboard/report_form.html"
    model = Report
    fields = ["year", "title", "pdf_file", "description", "is_active"]
    success_url = reverse_lazy("report-list")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, _("تم إضافة التقرير بنجاح."))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, _("حدث خطأ أثناء إضافة التقرير. يرجى التحقق من البيانات.")
        )
        return super().form_invalid(form)


class ReportDetailView(LoginRequiredMixin, DetailView):
    """Dashboard view to view report details"""

    template_name = "main/dashboard/report_detail.html"
    model = Report
    context_object_name = "report"
    login_url = reverse_lazy("login")


class ReportDeleteView(LoginRequiredMixin, DeleteView):
    """Dashboard view to delete a report"""

    template_name = "main/dashboard/report_delete.html"
    model = Report
    success_url = reverse_lazy("report-list")
    login_url = reverse_lazy("login")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _("تم حذف التقرير بنجاح."))
        return super().delete(request, *args, **kwargs)


# -------------------- CHATBOT MANAGEMENT --------------------


class ChatbotListView(LoginRequiredMixin, ListView):
    """Dashboard view to list all chatbot Q&As"""

    template_name = "main/dashboard/chatbot_list.html"
    model = ChatbotQA
    context_object_name = "chatbot_qas"
    login_url = reverse_lazy("login")
    paginate_by = 20

    def get_queryset(self):
        return ChatbotQA.objects.all().order_by("order", "-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_qas_count"] = ChatbotQA.objects.filter(is_active=True).count()
        context["total_views"] = sum(
            ChatbotQA.objects.values_list("view_count", flat=True)
        )
        return context


class ChatbotCreateView(LoginRequiredMixin, CreateView):
    """Dashboard view to create a new chatbot Q&A"""

    template_name = "main/dashboard/chatbot_form.html"
    model = ChatbotQA
    fields = ["question", "answer", "keywords", "category", "order", "is_active"]
    success_url = reverse_lazy("chatbot-list")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, _("تم إضافة السؤال والجواب بنجاح."))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, _("حدث خطأ أثناء إضافة السؤال. يرجى التحقق من البيانات.")
        )
        return super().form_invalid(form)


class ChatbotUpdateView(LoginRequiredMixin, UpdateView):
    """Dashboard view to update a chatbot Q&A"""

    template_name = "main/dashboard/chatbot_edit.html"
    model = ChatbotQA
    fields = ["question", "answer", "keywords", "category", "order", "is_active"]
    success_url = reverse_lazy("chatbot-list")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, _("تم تحديث السؤال والجواب بنجاح."))
        return super().form_valid(form)


class ChatbotDetailView(LoginRequiredMixin, DetailView):
    """Dashboard view to view chatbot Q&A details"""

    template_name = "main/dashboard/chatbot_detail.html"
    model = ChatbotQA
    context_object_name = "qa"
    login_url = reverse_lazy("login")


class ChatbotDeleteView(LoginRequiredMixin, DeleteView):
    """Dashboard view to delete a chatbot Q&A"""

    template_name = "main/dashboard/chatbot_delete.html"
    model = ChatbotQA
    success_url = reverse_lazy("chatbot-list")
    login_url = reverse_lazy("login")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _("تم حذف السؤال والجواب بنجاح."))
        return super().delete(request, *args, **kwargs)


class ChatbotSearchView(View):
    """API view for chatbot search"""

    def post(self, request):
        from django.db.models import Q

        query = request.POST.get("query", "").strip()

        if not query:
            return JsonResponse(
                {"success": False, "message": _("يرجى إدخال سؤال.")}, status=400
            )

        # Search for matching Q&As
        qas = ChatbotQA.objects.filter(is_active=True)

        # Filter by question, answer, or keywords
        qas = qas.filter(
            Q(question__icontains=query)
            | Q(answer__icontains=query)
            | Q(keywords__icontains=query)
        )

        if qas.exists():
            # Get the best match (first one)
            best_match = qas.first()
            best_match.increment_view_count()

            # Get all matches
            results = [
                {
                    "id": qa.id,
                    "question": qa.question,
                    "answer": qa.answer,
                    "category": qa.category,
                }
                for qa in qas[:5]  # Limit to 5 results
            ]

            return JsonResponse(
                {
                    "success": True,
                    "results": results,
                    "best_match": {
                        "id": best_match.id,
                        "question": best_match.question,
                        "answer": best_match.answer,
                        "category": best_match.category,
                    },
                }
            )
        else:
            # No matches found
            return JsonResponse(
                {
                    "success": False,
                    "message": _("عذراً، لم نجد إجابة لسؤالك. يرجى التواصل معنا مباشرة."),
                }
            )


class ChatbotGetAllView(View):
    """API view to get all active chatbot Q&As"""

    def get(self, request):
        qas = ChatbotQA.objects.filter(is_active=True).order_by("order", "-created_at")

        # Group by category
        categories = {}
        for qa in qas:
            category = qa.category or _("عام")
            if category not in categories:
                categories[category] = []
            categories[category].append(
                {"id": qa.id, "question": qa.question, "answer": qa.answer}
            )

        return JsonResponse(
            {"success": True, "categories": categories, "total": qas.count()}
        )
