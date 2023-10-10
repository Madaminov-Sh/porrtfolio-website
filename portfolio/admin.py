from django.contrib import admin

from .models import Resume, Skills, Education, Certificate


class SkillsInline(admin.TabularInline):
    model = Skills


class EducationInline(admin.TabularInline):
    model = Education


class CertificateInline(admin.TabularInline):
    model = Certificate


class ResumeAdmin(admin.ModelAdmin):
    inlines = [EducationInline, SkillsInline, CertificateInline]

admin.site.register(Resume, ResumeAdmin)