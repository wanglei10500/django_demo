# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question,Choice
# Register your models here.
"""
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date','question_text']

admin.site.register(Question,QuestionAdmin)
"""
class ChoiceInline(admin.TabularInline):  #TabularInline 基于表格的
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)