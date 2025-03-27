from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ['user', 'generated_at']  # 'user' is auto-assigned, 'generated_at' is auto_now_add