from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'report_type', 'generated_at')
    list_filter = ('generated_at',)
    search_fields = ('user__username', 'report_type')
