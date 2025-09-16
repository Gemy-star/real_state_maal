# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Contact, JobRequest, ProjectRequest


class JobRequestForm(forms.ModelForm):
    class Meta:
        model = JobRequest
        fields = "__all__"
        labels = {
            "name": _("الاسم الثلاثي"),
            "field": _("التخصص"),
            "cv": _("المرفقات وشهادات الخبرة"),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            "name": _("الاسم"),
            "email": _("البريد الإلكتروني"),
            "phone": _("رقم الجوال"),
            "subject": _("العنوان"),
            "message": _("الرسالة"),
        }


class ProjectRequestForm(forms.ModelForm):
    class Meta:
        model = ProjectRequest
        fields = "__all__"
        labels = {
            "name": _("الاسم"),
            "email": _("بريدك الإلكتروني"),
            "phone": _("رقم جوالك"),
            "description": _("حدثنا عن مشروعك"),
            "project_file": _("أرفق ملفات تدعم فكرتك"),
        }
