from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50)  # e.g., "Monthly Summary"
    generated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()  # Store JSON, markdown, or plain text

    def __str__(self):
        return f"{self.user.username} - {self.report_type}"
