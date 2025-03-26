from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """
        This view should return a list of all transactions
        for the currently authenticated user.
        """
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set the user to the current user when creating a transaction.
        """
        serializer.save(user=self.request.user)