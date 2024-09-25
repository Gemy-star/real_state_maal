# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Contact)
admin.site.register(News)
admin.site.register(JobRequest)
admin.site.register(ProjectRequest)
