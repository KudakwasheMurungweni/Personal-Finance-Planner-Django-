from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_type', 'category', 'amount', 'date')
    list_filter = ('transaction_type', 'date')
    search_fields = ('user__username', 'category')
