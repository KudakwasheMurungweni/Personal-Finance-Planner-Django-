from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication  # Import JWTAuthentication
from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]  # Use JWTAuthentication
    permission_classes = [IsAuthenticated]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


    def get_queryset(self):
        # Only return reports for the currently authenticated user
        return Report.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user to the current user when creating a report
        serializer.save(user=self.request.user)