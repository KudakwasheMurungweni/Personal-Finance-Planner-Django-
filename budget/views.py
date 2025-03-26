from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from .models import Budget
from .serializers import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetSerializer

    def get_queryset(self):
        """
        Return a list of all budgets for the currently authenticated user.
        """
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set the user to the current user when creating a budget.
        """
        serializer.save(user=self.request.user)