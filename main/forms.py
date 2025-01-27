# -*- coding: utf-8 -*-
from django import forms

from .models import Contact, JobRequest, ProjectRequest


class JobRequestForm(forms.ModelForm):
    class Meta:
        model = JobRequest
        fields = "__all__"
        labels = {
            "name": " الاسم الثلاثي ",
            "field": " التخصص  ",
            "cv": " المرفقات وشهادات الخبرة ",
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            "name": "الأسم ",
            "email": " البريد الأكترونى ",
            "phone": " الجوال ",
            "subject": " العنوان ",
            "message": " الرسالة ",
        }


class ProjectRequestForm(forms.ModelForm):
    class Meta:
        model = ProjectRequest
        fields = "__all__"
        labels = {
            "name": "الأسم ",
            "email": " بريدك الأكترونى ",
            "phone": " رقم جوالك ",
            "description": "  حدثنا عن مشروعك ",
            "project_file": "  إرفق ملفت تدعم فكرتك   ",
        }
